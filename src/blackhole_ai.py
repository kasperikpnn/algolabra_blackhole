import random, time, math, copy
from blackhole_game import adjacency

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.best_moves = {} # Avaimena lauta tuplena, arvona paras siirto. Käytetään siirtojen järjestämisessä

    def process_turn(self, board, ai_number, player_number):
        """Kopioi pelitilanteen ennen siirtojen kokeilua."""
        self.board = board.copy()
        empty_spaces, neighbors = self.obtain_info() 
        score = self.calculate_score(board, neighbors)
        return self.iterative_deepening(ai_number, player_number, empty_spaces, neighbors, score, len(empty_spaces))

    def obtain_info(self):
        """Käytetään minimaxin alussa, muodostaa listan mahdollisista siirroista ja ruutujen naapurien määrästä."""
        empty_spaces = []
        neighbors = [2, 4, 4, 4, 6, 4, 4, 6, 6, 4, 4, 6, 6, 6, 4, 2, 4, 4, 4, 4, 2]
        for i in range(21): # 21 ruutua
            if self.board[i] is None:
                empty_spaces.append(i)
        for i in range(21):
            if self.board[i] is not None:
                for adj_space in adjacency[i]:
                    neighbors[adj_space]-=1
        return empty_spaces, neighbors
    
    def calculate_score(self, board, neighbors):
        score = 0
        for i in range(21):
            if board[i] is not None:
                if neighbors[i] == 0:
                    num, player = board[i]
                    score += num if player == 'AI' else -num
        return score

    def minimax(self, depth, alpha, beta, is_maximizing, ai_number, player_number, empty_spaces, neighbors, score):
        """Minimax-algoritmi tehostettuna alpha-beta -karsinnalla ja parhaan siirron muistamisella."""
        key = tuple(self.board)
        # Kun musta aukko on ainoastaan jäljellä
        if len(empty_spaces) == 1:
            if score >= 1:
                return (None, 1000) # Voitto
            elif score == 0:
                return (None, 0) # Tasapeli
            else:
                return (None, -1000) # Häviö
        if depth == 0:
            return (None, score)
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
                # Kopioidaan kaikki käsiteltävät listat
                new_neighbors = neighbors.copy()
                new_empty_spaces = empty_spaces.copy()
                new_score = score
                # Päivitetään naapurilistaa ja pisteytystä kokeiltavalle siirrolle
                for adj_space in adjacency[space]:
                    new_neighbors[adj_space]-=1
                    if new_neighbors[adj_space] == 0:
                        if self.board[adj_space] is not None:
                            num, player = self.board[adj_space]
                            new_score += num if player == 'AI' else -num
                new_empty_spaces.remove(space)
                self.board[space] = (ai_number, "AI") # tekoäly kokeilee siirtoa
                if new_neighbors[space] == 0:
                    new_score += ai_number
                new_score = self.minimax(depth-1, alpha, beta, False, ai_number+1, player_number, new_empty_spaces, new_neighbors, new_score)
                self.board[space] = None # perutaan siirto
                if new_score[1] > value:
                    value = new_score[1]
                    best_space = space
                elif new_score[1] == value:
                    if neighbors[space] < neighbors[best_space]:
                        # Vähemmän naapureita yhtä arvokkaalla siirrolla -> valitaan tämä siirto
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
                # Kopioidaan kaikki käsiteltävät listat
                new_neighbors = neighbors.copy()
                new_empty_spaces = empty_spaces.copy()
                new_score = score
                # Päivitetään naapurilistaa ja pisteytystä kokeiltavalle siirrolle
                for adj_space in adjacency[space]:
                    new_neighbors[adj_space]-=1
                    if new_neighbors[adj_space] == 0:
                        if self.board[adj_space] is not None:
                            num, player = self.board[adj_space]
                            new_score += num if player == 'AI' else -num
                new_empty_spaces.remove(space)
                self.board[space] = (player_number, "P1") # pelaaja kokeilee siirtoa
                if new_neighbors[space] == 0:
                    new_score -= player_number
                new_score = self.minimax(depth-1, alpha, beta, True, ai_number, player_number+1, new_empty_spaces, new_neighbors, new_score)
                self.board[space] = None # perutaan siirto
                if new_score[1] < value:
                    value = new_score[1]
                    best_space = space
                elif new_score[1] == value:
                    if neighbors[space] < neighbors[best_space]:
                        # Vähemmän naapureita yhtä arvokkaalla siirrolla -> valitaan tämä siirto
                        best_space = space
                beta = min(beta, value)
                if alpha > beta:
                    # alpha-beta katkaisu tapahtuu
                    break
            self.best_moves[key] = best_space
            return best_space, value

    def iterative_deepening(self, ai_number, player_number, empty_spaces, neighbors, score, max_depth=20, time_limit=2.0):
        """Iteratiivinen syveneminen. Aikarajaksi asetettu 2 sekuntia."""
        best_space = None
        start_time = time.time()
        # max_depth on tässä aina len(empty_spaces), eli jäljellä olevien siirtojen määrä
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                # ei tiukkaa aikakatkaisua: kunhan uuden syvyyden tutkiminen aloitetaan ennen kuin aikaraja menee umpeen, se sallitaan
                # debug: print("päästiin syvyyteen " + str(depth-1))
                break
            space, value = self.minimax(depth, -math.inf, math.inf, True, ai_number, player_number, empty_spaces, neighbors, score)
            # debug: print("syvyys: " + str(depth) + ", paras siirto: " + str(space) + ", arvo: " + str(value))
            if space is not None:
                best_space = space
        return best_space, value