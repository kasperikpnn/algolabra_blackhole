import random, time, math
from blackhole_game import adjacency, find_black_hole, compute_scores

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.ai_number = 0
        self.player_number = 0
        self.best_moves = {}

    def createSumList(self):
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        sumlist = []
        for i in range(21):
            if self.board[i] == None:
                score = self.compute_score(i, self.board)
                sumlist.append(score)
            else:
                sumlist.append(None)
        return sumlist

    def compute_score(self, black_hole_pos, board):
        """Laskee kummankin pelaajan summan ruudun ympärillä."""
        adjacent = adjacency[black_hole_pos]
        player_sums = {"P1": 0, "AI": 0}
        for pos in adjacent:
            if board[pos]:
                num, player = board[pos]
                player_sums[player] += num
        return player_sums["P1"]-player_sums["AI"]

    def process_turn(self, board, ai_number, player_number):
        """Kopioi pelitilanteen ja jäljellä olevat numerot ennen kuin kokeillaan eri siirtoja."""
        self.board = board.copy()
        self.ai_number = ai_number
        self.player_number = player_number
        sums = self.createSumList()
        empty_spaces = self.get_empty_spaces()
        return self.iterative_deepening(ai_number, player_number, empty_spaces, sums)

    def get_empty_spaces(self):
        """Käytetään minimaxin alussa, muodostaa listan mahdollisista siirroista."""
        empty_spaces = []
        for i in range(21): # 21 ruutua
            if self.board[i] == None:
                empty_spaces.append(i)
        return empty_spaces

    def score(self, scores):
        """Varmistaa, onko ruutu tällä hetkellä tai pelin lopussa voittava tekoälylle."""
        return scores["P1"]-scores["AI"]

    def is_winning_board(self, sums):
        """Käytetään, kun laudalla on enää vain musta aukko jäljellä."""
        black_hole = next(i for i, x in enumerate(sums) if x is not None)
        return sums[black_hole] >= 1
    
    def make_AI_move(self, space, ai_number):
        """Tekee tekoälyn kokeiltavan siirron minimaxissa."""
        self.board[space] = (ai_number, "AI")

    def make_player_move(self, space, player_number):
        """Tekee pelaajan kokeiltavan siirron minimaxissa."""
        self.board[space] = (player_number, "P1")

    def undo_AI_move(self, space):
        """Peruu tekoälyn kokeiltavan siirron minimaxissa."""
        self.board[space] = None

    def undo_player_move(self, space):
        """Peruu pelaajan kokeiltavan siirron minimaxissa."""
        self.board[space] = None
    
    def evaluate(self, sums):
        only_int_sums = [x for x in sums if x is not None]
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        return sum(x > 0 for x in only_int_sums) - sum(x < 0 for x in only_int_sums)

    def minimax(self, depth, alpha, beta, isMaximizing, ai_number, player_number, empty_spaces, sums):
        """Minimax-algoritmi tehostettuna alpha-beta -karsinnalla ja parhaan siirron muistamisella."""
        if len(empty_spaces) == 1: ## Kun musta aukko on ainoastaan jäljellä
            if self.is_winning_board(sums):
                return (None, math.inf)
            elif self.is_winning_board(sums) == False:
                return (None, -math.inf)
            else: ## Tasapeli
                return (None, 0)
        if depth == 0:
            return (None, self.evaluate(sums))
        
        if isMaximizing: ## maksimointi
            str_board = str(self.board)
            prev_best_move = self.best_moves.get(str_board)
            if prev_best_move in empty_spaces:
                empty_spaces.remove(prev_best_move)
                empty_spaces.insert(0, prev_best_move)
            value = -math.inf
            best_space = None
            for space in empty_spaces:
                for adj_space in adjacency[space]:
                    if sums[adj_space] != None:
                        sums[adj_space]-=ai_number
                new_sums = sums[:space] + [None] + sums[space+1:]
                new_score = self.minimax(depth-1, alpha, beta, False, ai_number+1, player_number, [s for s in empty_spaces if s != space], new_sums)
                for adj_space in adjacency[space]:
                    if sums[adj_space] != None:
                        sums[adj_space]+=ai_number
                if new_score[1] >= value:
                    value = new_score[1]
                    best_space = space
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            self.best_moves[str_board] = best_space
            return best_space, value
        else: ## minimointi
            value = math.inf
            best_space = None
            for space in empty_spaces:
                for adj_space in adjacency[space]:
                    if sums[adj_space] != None:
                        sums[adj_space]+=ai_number
                new_sums = sums[:space] + [None] + sums[space+1:]
                new_score = self.minimax(depth-1, alpha, beta, True, ai_number, player_number+1, [s for s in empty_spaces if s != space], new_sums)
                for adj_space in adjacency[space]:
                    if sums[adj_space] != None:
                        sums[adj_space]-=ai_number
                if new_score[1] <= value:
                    value = new_score[1]
                    best_space = space
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_space, value

    def iterative_deepening(self, ai_number, player_number, empty_spaces, sums, max_depth=20, time_limit=5.0):
        """Iteratiivinen syveneminen. Aikarajaksi asetettu 5 sekuntia toistaiseksi. Max depth = 20 sallii tällä hetkellä pelin läpikäymisen ihan loppuun asti."""
        best_space = None
        start_time = time.time()
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                print("päästiin syvyyteen " + str(depth))
                break
            space, value = self.minimax(depth, -math.inf, math.inf, True, ai_number, player_number, empty_spaces, sums)
            if space is not None:
                best_space = space
        return best_space, value