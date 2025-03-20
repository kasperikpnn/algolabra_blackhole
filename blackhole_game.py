# Muuttujat

board = [None] * 21

player_numbers = {
    "P1": set(range(1, 11)),
    "AI": set(range(1, 11)),
}

current_turn = "P1"

# Määrittelee jokaisen ruudun viereiset ruudut. Käytetään pelin lopussa, kun viimeisestä ruudusta tulee "black hole".
adjacency = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1, 4, 5],
    3: [1, 4, 6, 7],
    4: [1, 2, 3, 5, 7, 8],
    5: [2, 4, 8, 9],
    6: [3, 7, 10, 11],
    7: [3, 4, 6, 8, 11, 12],
    8: [4, 5, 7, 9, 12, 13],
    9: [5, 8, 13, 14],
    10: [6, 11, 15, 16],
    11: [6, 7, 10, 12, 16, 17],
    12: [7, 8, 11, 13, 17, 18],
    13: [8, 9, 12, 14, 18, 19],
    14: [9, 13, 19, 20],
    15: [10, 16],
    16: [10, 11, 15, 17],
    17: [11, 12, 16, 18],
    18: [12, 13, 17, 19],
    19: [13, 14, 18, 20],
    20: [14, 19],
}

# Funktiot
def display_board():
    """Näyttää tämänhetkisen laudan tilanteen."""
    layout = [
        [0],
        [1, 2],
        [3, 4, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20]
    ]
    for row in layout:
        row_str = " ".join(format_slot(pos) for pos in row)
        print(" " * (15 - len(row) * 2), row_str)
    print()

def format_slot(pos):
    """Formatoi yksittäisen ruudun tekstin."""
    if board[pos] is None:
        return f"({pos:2})"  # Tyhjä ruutu -> palauttaa ruudun sijaintinumeron
    else:
        num, player = board[pos]
        return f"({player}:{num:2})" # Täytetty ruutu -> palauttaa ruudun tässä muodossa: P1:3 tai CPU:2
    
def get_input(current_player):
    """Käytännössä if-lause: jos on pelaajan vuoro niin jatketaan funktiolle get_player_input, jos tekoälyn vuoro niin get_ai_input."""

def get_player_input():
    """Käydään yksittäinen pelaajan vuoro läpi. Pelaajan tarvitsee kirjoittaa vain ruudun sijaintinumero terminaaliin sijoittaakseen oman numeronsa ja pelatakseen vuoronsa."""

def get_ai_input():
    """Käydään tekoälyn vuoro läpi. (Tekoälyn koodi tulee sijaitsemaan eri .py tiedostossa) Aluksi tekoäly toteutetaan vain niin, että se tekee sattumanvaraisen vuoron, kunnes pelin toteutus on kunnossa."""

display_board()