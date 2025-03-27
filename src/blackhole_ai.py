import random, time, math
from blackhole_game import adjacency, find_black_hole, compute_scores

class BlackHoleAI:
    def __init__(self):
        self.board = [None] * 21
        self.ai_numbers = list(range(1, 11))
        self.player_numbers = list(range(1, 11))
        self.best_moves = {}

    def process_turn(self, board, ai_numbers, player_numbers):
        self.board = board.copy()
        self.ai_numbers = ai_numbers.copy()
        self.player_numbers = player_numbers.copy()
        return self.iterative_deepening()

    def get_empty_spaces(self):
        empty_spaces = []
        for i in range(21): # 21 ruutua
            if self.board[i] == None:
                empty_spaces.append(i)
        return empty_spaces

    def is_winning_score(self, scores):
        if scores["P1"] > scores["AI"]:
            return True
        elif scores["P1"] == scores["AI"]:
            return None
        else:
            return False

    def is_winning_board(self):
        black_hole = find_black_hole(self.board)
        scores = compute_scores(black_hole, self.board)
        return self.is_winning_score(scores)
    
    def make_AI_move(self, space):
        self.board[space] = (self.ai_numbers[0], "AI")
        self.ai_numbers.pop(0)

    def make_player_move(self, space):
        self.board[space] = (self.player_numbers[0], "AI")
        self.player_numbers.pop(0)

    def undo_AI_move(self, space):
        self.board[space] = None
        if len(self.ai_numbers) >= 1:
            self.ai_numbers.insert(0, self.ai_numbers[0]-1)
        else:
            self.ai_numbers = [10]

    def undo_player_move(self, space):
        self.board[space] = None
        if len(self.player_numbers) >= 1:
            self.player_numbers.insert(0, self.player_numbers[0]-1)
        else:
            self.player_numbers = [10]
    
    def evaluate(self):
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

    def minimax(self, depth, alpha, beta, isMaximizing):
        empty_spaces = self.get_empty_spaces()
        if len(empty_spaces) == 1:
            if self.is_winning_board():
                return (None, math.inf)
            elif self.is_winning_board() == False:
                return (None, -math.inf)
            else: ## Tasapeli
                return (None, 0)
        if depth == 0:
            return (None, self.evaluate())
        
        if isMaximizing:
            tuple_board = tuple(self.board)
            prev_best_move = self.best_moves.get(tuple_board)
            if prev_best_move in empty_spaces:
                empty_spaces.remove(prev_best_move)
                empty_spaces.insert(0, prev_best_move)
            value = -math.inf
            best_space = None
            for space in empty_spaces:
                self.make_AI_move(space)
                new_score = self.minimax(depth-1, alpha, beta, False)
                self.undo_AI_move(space)
                print(new_score)
                print(value)
                if new_score[1] > value:
                    value = new_score[1]
                    best_space = space
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            self.best_moves[tuple_board] = best_space
            return best_space, value
        else:
            value = math.inf
            best_space = None
            for space in empty_spaces:
                self.make_player_move(space)
                new_score = self.minimax(depth-1, alpha, beta, True)
                self.undo_player_move(space)
                if new_score[1] < value:
                    value = new_score[1]
                    best_space = space
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_space, value

    def iterative_deepening(self, max_depth=6, time_limit=2.0):
        best_space = None
        start_time = time.time()
        for depth in range(1, max_depth+1):
            if time.time() - start_time > time_limit:
                break
            space, value = self.minimax(depth, -math.inf, math.inf, True)
            if space is not None:
                best_space = space
        return best_space