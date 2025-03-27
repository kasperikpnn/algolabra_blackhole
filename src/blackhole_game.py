import random

# Muuttujat

board = [None] * 21

player_numbers = {
    "P1": list(range(1, 11)),
    "AI": list(range(1, 11)),
}

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
    
def get_input(current_player, turn_number):
    """Käytännössä vain if-lause, joka antaa vuoron joko pelaajalle tai tekoälylle."""
    if current_player == "P1":
        return get_player_input(turn_number)
    elif current_player == "AI":
        return get_ai_input(turn_number)
    else:
        return -1 # Ei ollut pelaajan eikä AI:n vuoro (tämän ei pitäisi tapahtua)

def get_player_input(turn_number):
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

def get_ai_input(turn_number):
    """Käsittelee tekoälyn vuoron. Pääasiassa oikeastaan vain kutsuu blackhole_ai.process_turn ja palauttaa saadun position."""
    print(f"[VUORO {turn_number}] Tekoälyn vuoro!")
    num, pos = player_numbers["AI"][0], bh_ai.process_turn(board, player_numbers["AI"], player_numbers["P1"])
    print(f"Tekoäly: Hmm, taidanpa asettaa luvun {num} ruutuun {pos[0]}. (Arvo: {pos[1]})")
    return num, pos[0]

def find_black_hole(board):
    """Käytetään pelin lopussa mustan aukon löytämiseksi. Palauttaa ruudun sijaintinumeron."""
    for i, val in enumerate(board):
        if val is None:
            return i
    return -2 # Mustaa aukkoa ei löytynyt (tämän ei pitäisi tapahtua)

def compute_scores(black_hole_pos, board):
    """Laskee kummankin pelaajan summan mustan aukon ympärillä."""
    adjacent = adjacency[black_hole_pos]
    player_sums = {"P1": 0, "AI": 0}
    for pos in adjacent:
        if board[pos]:
            num, player = board[pos]
            player_sums[player] += num
    return player_sums

def game():
    """Peli"""
    print("Black Holen säännöt:")
    print("1. Pelaajat asettavat pyramidilaudalle vuorotellen numeroita aloittaen luvusta 1 ja päättyen lukuun 10.")
    print("2. Viimeisellä vuorolla tyhjäksi jääneestä solusta muodostuu musta aukko.")
    print("3. Pelin lopussa lasketaan kummankin pelaajan numeroiden summa mustan aukon ympärillä - pelaaja, jolla on pienempi summa voittaa!\n")
    display_board()
    players = ["P1", "AI"]
    current_player = random.choice(players)
    turn_number = 1
    for i in range(20):
        num, pos = get_input(current_player, turn_number)
        board[pos] = (num, current_player)
        player_numbers[current_player].pop(0)
        display_board()
        current_player = "AI" if current_player == "P1" else "P1"
        turn_number+=1

    black_hole = find_black_hole(board)
    print(f"Musta aukko muodostui ruutuun {black_hole}!!")

    scores = compute_scores(black_hole, board)
    print(f"\nPelaajien summat:")
    print(f"Pelaaja: {scores["P1"]}")
    print(f"Tekoäly: {scores["AI"]}")

    if scores["P1"] < scores["AI"]:
        print("Pelaaja voitti! :)")
    elif scores["AI"] < scores["P1"]:
        print("Tekoäly voitti! :(")
    else:
        print("Tasapeli :/")

if __name__ == "__main__":
    import blackhole_ai
    bh_ai = blackhole_ai.BlackHoleAI()
    game()