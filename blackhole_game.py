import blackhole_ai
import random

# Muuttujat

board = [None] * 21

player_numbers = {
    "P1": list(range(1, 11)),
    "AI": list(range(1, 11)),
}

players = ["P1", "AI"]
current_turn = random.choice(players)

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
        return f"({str(pos).center(5)})"  # Tyhjä ruutu -> palauttaa ruudun sijaintinumeron
    else:
        num, player = board[pos]
        return f"({player}:{num:2})".center(7) # Täytetty ruutu -> palauttaa ruudun tässä muodossa: P1:3 tai CPU:2
    
def get_input():
    if current_turn == "P1":
        return get_player_input()
    elif current_turn == "AI":
        return get_ai_input()
    else:
        return -1 # Ei ollut pelaajan eikä AI:n vuoro (tämän ei pitäisi tapahtua)

def get_player_input():
    """Käydään yksittäinen pelaajan vuoro läpi. Pelaajan tarvitsee kirjoittaa vain ruudun sijaintinumero terminaaliin sijoittaakseen oman numeronsa ja pelatakseen vuoronsa."""
    while True:
        try:
            print(f"[VUORO {turn_number}] Pelaajan vuoro! Aika asettaa laudalle numero {player_numbers["P1"][0]}")
            pos = int(input("Valitse tyhjä ruutu kirjoittamalla ruudun sijaintinumero (0-20): "))
            if pos < 0 or pos >= 21 or board[pos] is not None:
                print("Numero ei ole välillä 0-20 tai ruutu on jo täytetty!")
                continue

            return player_numbers["P1"][0], pos
        except ValueError:
            print("Virheellinen syöte!") 

def get_ai_input():
    print(f"[VUORO {turn_number}] Tekoälyn vuoro!")
    num, pos = blackhole_ai.process_turn(board, turn_number, player_numbers["AI"])
    print(f"Tekoäly: Hmm, taidanpa asettaa luvun {num} ruutuun {pos}.")
    return num, pos

def find_black_hole():
    """Käytetään pelin lopussa mustan aukon löytämiseksi. Palauttaa ruudun sijaintinumeron."""
    for i, val in enumerate(board):
        if val is None:
            return i
    return -2 # Mustaa aukkoa ei löytynyt (tämän ei pitäisi tapahtua)

def compute_scores(black_hole_pos):
    """Laskee kummankin pelaajan summan mustan aukon ympärillä."""
    adjacent = adjacency[black_hole_pos]
    player_sums = {"P1": 0, "AI": 0}
    for pos in adjacent:
        if board[pos]:
            num, player = board[pos]
            player_sums[player] += num
    return player_sums

# Peli

print("Black Holen säännöt:")
print("1. Pelaajat asettavat vuorotellen numeroita aloittaen luvusta 1 ja päättyen lukuun 10.")
print("2. Yksi laudan ruuduista jää lopulta tyhjäksi, ja tästä ruudusta tulee musta aukko.")
print("3. Tavoite on minimoida omien numeroiden summa mustan aukon ympärillä - se pelaaja jolla on pienempi summa voittaa!\n")

display_board()

turn_number = 1
for i in range(20):
    num, pos = get_input()
    board[pos] = (num, current_turn)
    player_numbers[current_turn].pop(0)
    display_board()
    current_turn = "AI" if current_turn == "P1" else "P1"
    turn_number+=1

black_hole = find_black_hole()
print(f"Musta aukko jäi ruutuun {black_hole}!!")

scores = compute_scores(black_hole)
print(f"\nPelaajien summat:")
print(f"Pelaaja: {scores["P1"]}")
print(f"Tekoäly: {scores["AI"]}")

if scores["P1"] < scores["AI"]:
    print("Pelaaja voitti! :)")
elif scores["AI"] < scores["P1"]:
    print("Tekoäly voitti! :(")
else:
    print("Tasapeli :/")

display_board()