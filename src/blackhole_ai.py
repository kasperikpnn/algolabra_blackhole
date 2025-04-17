import random, time, math
from blackhole_game import adjacency, find_black_hole, compute_scores

rotation_maps = [

    # 0° (alkuperäinen lauta)
    list(range(21)),

    # 0° peilattuna
    [0, 2, 1, 5, 4, 3, 9, 8, 7, 6, 14, 13, 12, 11, 10, 20, 19, 18, 17, 16, 15],

    # 120° (lauta käännettynä 120 astetta)
    [15, 16, 10, 17, 11, 6, 18, 12, 7, 3, 19, 13, 8, 4, 1, 20, 14, 9, 5, 2, 0],

    # 120° peilattuna
    [15, 10, 16, 6, 11, 17, 3, 7, 12, 18, 1, 4, 8, 13, 19, 0, 2, 5, 9, 14, 20],

    # 240° (lauta käännettynä 240 astetta)
    [20, 14, 19, 9, 13, 18, 5, 8, 12, 17, 2, 4, 7, 11, 16, 0, 1, 3, 6, 10, 15],

    # 240° peilattuna
    [20, 19, 14, 18, 13, 9, 17, 12, 8, 5, 16, 11, 7, 4, 2, 15, 10, 6, 3, 1, 0]
]

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.ai_number = 0
        self.player_number = 0
        self.best_moves = {}

    def canonical_board(self, board):
        """Palauttaa pelilaudan tilanteen pienimmän symmetrisen muodon."""
        if board is None or any(b is not None and not isinstance(b, tuple) for b in board):
            raise ValueError("Laudan muoto on virheellinen: " + str(board))
        rotation_hashes = []
        for rotation in rotation_maps:
            rotated = tuple(board[rotation[i]] for i in range(21))
            rotation_hashes.append(hash(rotated))
        return min(rotation_hashes)

    def process_turn(self, board, ai_number, player_number):
        """Kopioi pelitilanteen ja jäljellä olevat numerot ennen kuin kokeillaan eri siirtoja."""
        self.board = board.copy()
        self.ai_number = ai_number
        self.player_number = player_number
        empty_spaces = self.get_empty_spaces()
        return self.iterative_deepening(ai_number, player_number, empty_spaces)

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

    def is_winning_board(self):
        """Käytetään, kun laudalla on enää vain musta aukko jäljellä."""
        black_hole = find_black_hole(self.board)
        scores = compute_scores(black_hole, self.board)
        print(self.score(scores))
        print(self.score(scores) >= 1)
        return self.score(scores) >= 1
    
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
    
    def evaluate(self):
        """Arvioi pelitilanteen. Heuristiikkana tekoälyn senhetkisten voittoruutujen määrä miinus pelaajan senhetkisten voittoruutujen määrä."""
        winning_spaces = 0
        losing_spaces = 0
        for i in range(21):
            if self.board[i] == None:
                scores = compute_scores(i, self.board)
                if self.is_winning_score(scores):
                    winning_spaces+=1
                elif self.is_winning_score(scores) == False:
                    losing_spaces+=1
        return winning_spaces - losing_spaces

    def minimax(self, depth, alpha, beta, isMaximizing, ai_number, player_number, empty_spaces):
        """Minimax-algoritmi tehostettuna alpha-beta -karsinnalla ja parhaan siirron muistamisella."""
        if len(empty_spaces) == 1: ## Kun musta aukko on ainoastaan jäljellä
            if self.is_winning_board():
                return (None, math.inf)
            elif self.is_winning_board() == False:
                return (None, -math.inf)
            else: ## Tasapeli
                return (None, 0)
        if depth == 0:
            return (None, self.evaluate())
        
        if isMaximizing: ## maksimointi
            str_board = str(self.board)
            prev_best_move = self.best_moves.get(str_board)
            if prev_best_move in empty_spaces:
                empty_spaces.remove(prev_best_move)
                empty_spaces.insert(0, prev_best_move)
            value = -math.inf
            best_space = None
            canon_boards = []
            for space in empty_spaces:
                self.make_AI_move(space, ai_number)
                canon = self.canonical_board(self.board)
                if canon not in canon_boards:
                    new_score = self.minimax(depth-1, alpha, beta, False, ai_number+1, player_number, [s for s in empty_spaces if s != space])
                    self.undo_AI_move(space)
                    if new_score[1] >= value:
                        value = new_score[1]
                        best_space = space
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
                    canon_boards.append(canon)
                else:
                    self.undo_AI_move(space)
                    continue
            self.best_moves[str_board] = best_space
            return best_space, value
        else: ## minimointi
            value = math.inf
            best_space = None
            opp_canon_boards = []
            for space in empty_spaces:
                self.make_player_move(space, player_number)
                opp_canon = self.canonical_board(self.board)
                if opp_canon not in opp_canon_boards:
                    new_score = self.minimax(depth-1, alpha, beta, True, ai_number, player_number+1, [s for s in empty_spaces if s != space])
                    self.undo_player_move(space)
                    if new_score[1] <= value:
                        value = new_score[1]
                        best_space = space
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
                    opp_canon_boards.append(opp_canon)
                else:
                    self.undo_player_move(space)
                    continue
            return best_space, value

    def iterative_deepening(self, ai_number, player_number, empty_spaces, max_depth=10, time_limit=5.0):
        """Iteratiivinen syveneminen. Aikarajaksi asetettu 5 sekuntia toistaiseksi. Max depth = 20 sallii tällä hetkellä pelin läpikäymisen ihan loppuun asti."""
        best_space = None
        start_time = time.time()
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                print("päästiin syvyyteen " + str(depth))
                break
            space, value = self.minimax(depth, -math.inf, math.inf, True, ai_number, player_number, empty_spaces)
            if space is not None:
                best_space = space
        return best_space, value