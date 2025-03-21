import random

def process_turn(board, turn_number, ai_numbers):
    """Käsittelee tekoälyn vuoron."""
    possible_positions = []
    for i in range(21): # 21 ruutua
        if board[i] == None:
            possible_positions.append(i)
    choice = random.choice(possible_positions)
    return ai_numbers[0], choice
    
        