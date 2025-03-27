import random
from blackhole_game import adjacency, find_black_hole, compute_scores

def process_turn(board, turn_number, ai_numbers):
    """Käsittelee tekoälyn vuoron."""
    possible_positions = []
    for i in range(21): # 21 ruutua
        if board[i] == None:
            possible_positions.append(i)
    choice = random.choice(possible_positions)
    return ai_numbers[0], choice

def evaluate(board):
    winning_spaces = 0
    equal_spaces = 0
    losing_spaces = 0
    for i in range(21):
        if board[i] == None:
            scores = compute_scores(i, board)
            if is_winning_score(scores):
                winning_spaces+=1
            elif is_winning_score(scores) == None:
                equal_spaces+=1
            elif is_winning_score(scores) == False:
                losing_spaces+=1
    return winning_spaces - losing_spaces

def is_winning_score(scores):
    if scores["P1"] > scores["AI"]:
        return True
    elif scores["P1"] == scores["AI"]:
        return None
    else:
        return False

def is_winning_board(board):
    black_hole = find_black_hole(board)
    scores = compute_scores(black_hole, board)
    return is_winning_score(scores)