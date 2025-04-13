import random, time, math
from blackhole_game import adjacency, find_black_hole, compute_scores

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.best_moves = {}
        self.help_table = {} ## avaimena lauta, arvona (heuristinen arvo, summalista)

    def process_turn(self, board, ai_number, player_number):
        """Kopioi pelitilanteen ja jäljellä olevat numerot ennen kuin kokeillaan eri siirtoja."""
        self.board = board.copy()
        empty_spaces = self.get_empty_spaces()
        sums = self.createSumList()
        value = self.evaluate(sums)
        return self.iterative_deepening(ai_number, player_number, empty_spaces, sums, value)

    def get_empty_spaces(self):
        """Käytetään minimaxin alussa, muodostaa listan mahdollisista siirroista."""
        empty_spaces = []
        for i in range(21): # 21 ruutua
            if self.board[i] == None:
                empty_spaces.append(i)
        return empty_spaces

    def is_winning_score(self, scores):
        """Varmistaa, onko ruutu tällä hetkellä tai pelin lopussa voittava tekoälylle."""
        if scores["P1"] > scores["AI"]:
            return True
        elif scores["P1"] == scores["AI"]:
            return None
        else:
            return False

    def is_winning_board(self):
        """Käytetään, kun laudalla on enää vain musta aukko jäljellä."""
        black_hole = find_black_hole(self.board)
        scores = compute_scores(black_hole, self.board)
        return self.is_winning_score(scores)
    
    def compute_score(self, black_hole_pos, board):
        """Laskee kummankin pelaajan summan ruudun ympärillä."""
        adjacent = adjacency[black_hole_pos]
        player_sums = {"P1": 0, "AI": 0}
        for pos in adjacent:
            if board[pos]:
                num, player = board[pos]
                player_sums[player] += num
        return player_sums["P1"]-player_sums["AI"]

    def createSumList(self):
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        sumlist = []
        for i in range(21):
            if self.board[i] == None:
                score = self.compute_score(i, self.board)
                sumlist.append(score)
            else:
                sumlist.append(0)
        return sumlist
    
    def evaluate(self, sumlist):
        if self.help_table.get(tuple(self.board)):
            return self.help_table[tuple(self.board)][0]
        else:
            value = sum(x > 0 for x in sumlist) - sum(x < 0 for x in sumlist)
            self.help_table[tuple(self.board)] = (value, sumlist)
        return value

    def minimax(self, depth, alpha, beta, isMaximizing, ai_number, player_number, empty_spaces, sums, value):
        """Minimax-algoritmi tehostettuna alpha-beta -karsinnalla ja parhaan siirron muistamisella."""
        if ai_number == 11 and player_number == 11: ## Kun musta aukko on ainoastaan jäljellä
            if self.is_winning_board():
                return (None, math.inf)
            elif self.is_winning_board() == False:
                return (None, -math.inf)
            else: ## Tasapeli
                return (None, 0)
        if depth == 0:
            return (None, self.evaluate(sums))

        if isMaximizing: ## maksimointi
            tuple_board = tuple(self.board) ## Täytyy muuttaa tupleksi dictionaryä varten
            prev_best_move = self.best_moves.get(tuple_board)
            if prev_best_move in empty_spaces:
                empty_spaces.remove(prev_best_move)
                empty_spaces.insert(0, prev_best_move)
            max_value = -math.inf
            best_space = None
            for space in empty_spaces:
                self.board[space] = (ai_number, "AI")
                storedsum = sums[space]
                if self.help_table.get(tuple(self.board)):
                    sums = self.help_table[tuple(self.board)][1].copy()
                else:
                    sums[space] = 0
                    for adj_space in adjacency[space]:
                        sums[adj_space]-=ai_number
                new_score = self.minimax(depth-1, alpha, beta, False, ai_number+1, player_number, [s for s in empty_spaces if s != space], sums.copy(), value)
                self.board[space] = None
                if self.help_table.get(tuple(self.board)):
                    sums = self.help_table[tuple(self.board)][1].copy()
                else:
                    sums[space] = storedsum
                    for adj_space in adjacency[space]:
                        sums[adj_space]+=ai_number
                if new_score[1] >= max_value:
                    max_value = new_score[1]
                    best_space = space
                alpha = max(alpha, max_value)
                if alpha >= beta:
                    break
            self.best_moves[tuple_board[:]] = best_space
            return best_space, max_value
        else: ## minimointi
            min_value = math.inf
            best_space = None
            for space in empty_spaces:
                self.board[space] = (player_number, "P1")
                storedsum = sums[space]
                if self.help_table.get(tuple(self.board)):
                    sums = self.help_table[tuple(self.board)][1].copy()
                else:
                    sums[space] = 0
                    for adj_space in adjacency[space]:
                        sums[adj_space]+=player_number
                new_score = self.minimax(depth-1, alpha, beta, True, ai_number, player_number+1, [s for s in empty_spaces if s != space], sums.copy(), value)
                self.board[space] = None
                if self.help_table.get(tuple(self.board)):
                    sums = self.help_table[tuple(self.board)][1].copy()
                else:
                    sums[space] = storedsum
                    for adj_space in adjacency[space]:
                        sums[adj_space]-=player_number
                if new_score[1] <= min_value:
                    min_value = new_score[1]
                    best_space = space
                beta = min(beta, min_value)
                if alpha >= beta:
                    break
            return best_space, min_value

    def iterative_deepening(self, ai_number, player_number, empty_spaces, sums, value, max_depth=20, time_limit=5.0):
        """Iteratiivinen syveneminen. Aikarajaksi asetettu 2 sekuntia toistaiseksi. Max depth = 20 sallii tällä hetkellä pelin läpikäymisen ihan loppuun asti."""
        best_space = None
        start_time = time.time()
        best_value = 0
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                break
            space, iteration_value = self.minimax(depth, -math.inf, math.inf, True, ai_number, player_number, empty_spaces, sums, value)
            if space is not None:
                best_space = space
                best_value = iteration_value
        print("Päästiin syvyyteen " + str(depth))
        return best_space, best_value