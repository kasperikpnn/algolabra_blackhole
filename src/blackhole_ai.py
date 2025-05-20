import random, time, math, copy
from blackhole_game import adjacency

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.best_moves = {} # Avaimena lauta tuplena, arvona paras siirto. Käytetään siirtojen järjestämisessä

    def create_sum_list(self, board):
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        sumlist = []
        for i in range(21):
            if board[i] == None:
                score = self.compute_score(i, board)
                sumlist.append(score)
            else:
                sumlist.append(None)
        return sumlist

    def compute_score(self, black_hole_pos, board):
        """Laskee kummankin pelaajan summan yksittäisen ruudun ympärillä."""
        adjacent = adjacency[black_hole_pos]
        player_sums = {"P1": 0, "AI": 0}
        for pos in adjacent:
            if board[pos]:
                num, player = board[pos]
                player_sums[player] += num
        # positiivinen summa = pelaajalla on suurempi summa, negatiivinen summa = tekoälyllä on suurempi summa
        return player_sums["P1"]-player_sums["AI"]

    def process_turn(self, board, ai_number, player_number):
        """Kopioi pelitilanteen ja jäljellä olevat numerot ennen kuin kokeillaan eri siirtoja."""
        self.board = board.copy()
        sums = self.create_sum_list(self.board)
        empty_spaces, neighbors = self.obtain_info() 
        return self.iterative_deepening(ai_number, player_number, empty_spaces, sums, neighbors, len(empty_spaces))

    def obtain_info(self):
        """Käytetään minimaxin alussa, muodostaa listan mahdollisista siirroista ja ruutujen naapurien määrästä."""
        empty_spaces = []
        neighbors = [2, 4, 4, 4, 6, 4, 4, 6, 6, 4, 4, 6, 6, 6, 4, 2, 4, 4, 4, 4, 2]
        for i in range(21): # 21 ruutua
            if self.board[i] == None:
                empty_spaces.append(i)
            else:
                neighbors[i] = None
        for i in range(21):
            if self.board[i] is not None:
                for adj_space in adjacency[i]:
                    if neighbors[adj_space] is not None:
                        neighbors[adj_space]-=1
        return empty_spaces, neighbors
    
    def evaluate(self, sums, ai_number, player_number):
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        # Ruudut, joissa on ylivoimaisesti suurempi summa (suurempi kuin vastapelaajan seuraava numero) lasketaan kolminkertaisesti.
        only_int_sums = [x for x in sums if x is not None]
        return 2 * sum(x > ai_number for x in only_int_sums) + sum(x > 0 for x in only_int_sums) - sum(x < 0 for x in only_int_sums) - 2 * sum(x < -player_number for x in only_int_sums)

    def minimax(self, depth, alpha, beta, is_maximizing, ai_number, player_number, empty_spaces, sums, neighbors):
        """Minimax-algoritmi tehostettuna alpha-beta -karsinnalla ja parhaan siirron muistamisella."""
        key = tuple(self.board)
        # Kun musta aukko on ainoastaan jäljellä
        if len(empty_spaces) == 1:
            if sums[empty_spaces[0]] >= 1:
                return (None, 1000) # Voitto
            elif sums[empty_spaces[0]] == 0:
                return (None, 0) # Tasapeli
            else:
                return (None, -1000) # Häviö
        if depth == 0:
            return (None, self.evaluate(sums, ai_number, player_number))
        if is_maximizing: # maksimointi
            value = -math.inf
            best_space = None
            # Siirtojen järjestys
            valid_indexes = empty_spaces.copy()
            sorted_empty_spaces = sorted(valid_indexes, key=lambda i: neighbors[i]) # Järjestetään siirrot naapurien määrän mukaan (ruutu jolla on vähiten naapureita käydään läpi ensin)
            # Siirretään viimeksi havaittu paras siirto ensimmäiseksi järjestetyssä siirtolistassa
            prev_best_move = self.best_moves.get(key)
            if prev_best_move in sorted_empty_spaces:
                sorted_empty_spaces.remove(prev_best_move)
                sorted_empty_spaces.insert(0, prev_best_move)
            for space in sorted_empty_spaces:
                # Syväkopioidaan kaikki käsiteltävät listat
                new_sums = copy.deepcopy(sums)
                new_neighbors = copy.deepcopy(neighbors)
                new_empty_spaces = copy.deepcopy(empty_spaces)
                # Päivitetään summa- ja naapurilistaa kokeiltavalle siirrolle
                for adj_space in adjacency[space]:
                    if new_sums[adj_space] != None:
                        new_sums[adj_space]-=ai_number
                        new_neighbors[adj_space]-=1
                new_sums[space] = None
                new_neighbors[space] = None
                new_empty_spaces.remove(space)
                self.board[space] = (ai_number, "AI") # tekoäly kokeilee siirtoa
                new_score = self.minimax(depth-1, alpha, beta, False, ai_number+1, player_number, new_empty_spaces, new_sums, new_neighbors)
                self.board[space] = None # perutaan siirto
                if new_score[1] > value:
                    value = new_score[1]
                    best_space = space
                elif new_score[1] == value:
                    if neighbors[space] < neighbors[best_space]:
                        # Vähemmän naapureita yhtä arvokkaalla siirrolla -> valitaan tämä siirto
                        best_space = space
                    elif sums[space] > sums[best_space]:
                        # Jos yhtä arvokas siirto peittää ruudun jolla on suurempi summa -> valitaan tämä siirto
                        best_space = space
                alpha = max(alpha, value)
                if alpha > beta:
                    # alpha-beta katkaisu tapahtuu
                    break
            self.best_moves[key] = best_space
            return best_space, value
        else: # minimointi
            value = math.inf
            best_space = None
            # Siirtojen järjestys
            valid_indexes = empty_spaces.copy()
            sorted_empty_spaces = sorted(valid_indexes, key=lambda i: neighbors[i])
            # Siirretään viimeksi havaittu paras siirto ensimmäiseksi järjestetyssä siirtolistassa
            prev_best_move = self.best_moves.get(key)
            if prev_best_move in sorted_empty_spaces:
                sorted_empty_spaces.remove(prev_best_move)
                sorted_empty_spaces.insert(0, prev_best_move)
            for space in sorted_empty_spaces:
                # Syväkopioidaan kaikki käsiteltävät listat
                new_sums = copy.deepcopy(sums)
                new_neighbors = copy.deepcopy(neighbors)
                new_empty_spaces = copy.deepcopy(empty_spaces)
                # Päivitetään summa- ja naapurilistaa kokeiltavalle siirrolle
                for adj_space in adjacency[space]:
                    if new_sums[adj_space] != None:
                        new_sums[adj_space]+=player_number
                        new_neighbors[adj_space]-=1
                new_sums[space] = None
                new_neighbors[space] = None
                new_empty_spaces.remove(space)
                self.board[space] = (player_number, "P1") # pelaaja kokeilee siirtoa
                new_score = self.minimax(depth-1, alpha, beta, True, ai_number, player_number+1, new_empty_spaces, new_sums, new_neighbors)
                self.board[space] = None # perutaan siirto
                if new_score[1] < value:
                    value = new_score[1]
                    best_space = space
                elif new_score[1] == value:
                    if neighbors[space] < neighbors[best_space]:
                        # Vähemmän naapureita yhtä arvokkaalla siirrolla -> valitaan tämä siirto
                        best_space = space
                    elif sums[space] < sums[best_space]:
                        # Jos yhtä arvokas siirto peittää ruudun jolla on suurempi summa -> valitaan tämä siirto
                        best_space = space
                beta = min(beta, value)
                if alpha > beta:
                    # alpha-beta katkaisu tapahtuu
                    break
            self.best_moves[key] = best_space
            return best_space, value

    def iterative_deepening(self, ai_number, player_number, empty_spaces, sums, neighbors, max_depth=20, time_limit=2.0):
        """Iteratiivinen syveneminen. Aikarajaksi asetettu 2 sekuntia."""
        best_space = None
        start_time = time.time()
        # max_depth on tässä aina len(empty_spaces), eli jäljellä olevien siirtojen määrä
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                # ei tiukkaa aikakatkaisua: kunhan uuden syvyyden tutkiminen aloitetaan ennen kuin aikaraja menee umpeen, se sallitaan
                print("päästiin syvyyteen " + str(depth))
                break
            space, value = self.minimax(depth, -9999, 9999, True, ai_number, player_number, empty_spaces, sums, neighbors)
            print("syvyys: " + str(depth) + ", paras siirto: " + str(space) + ", arvo: " + str(value))
            if space is not None:
                best_space = space
        return best_space, value