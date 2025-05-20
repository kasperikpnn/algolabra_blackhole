# Testausdokumentti

## Yleinen kuvaus

Projektin yksikkötestaus on toteutettu pytestillä. Yksikkötestien lisäksi projektia on testattu empiirisesti.

## Yksikkötestit

Luokalle BlackHoleAI (sijaitsee blackhole_ai.py tiedostossa) on toteutettu yksikkötestit. Pelille ja sen käyttöliittymälle ei ole toteutettu testejä. Alla on jokainen testi järjestyksessä ja kategorioituna, ja lyhyt kuvaus testin tarkoituksesta.

### Luokan metodien testaus

#### test_create_sum_list

- toimiiko *create_sum_list* ja siinä käytetty *compute_score* toivotusti eräällä pelilaudan tilanteella, jossa on sekä tasapelejä että pelaajalle ja tekoälylle häviäviä ruutuja.

### Siirtojen laillisuuden testaus

#### test_valid_move_on_empty_board

- onko tekoälyn antama siirto laillinen ensimmäisellä siirrolla (jokin arvo välillä 0-20).

#### test_valid_move_at_very_end

- onko tekoälyn antama siirto laillinen viimeisellä siirrolla (yksi esimerkkipelilaudan tyhjistä ruuduista: 19 tai 20).

### Minimaxin testaus

#### test_minimax_loss

- tunnistaako minimax-algoritmi häviön selvästi häviävästä pelitilanteesta.

#### test_minimax_win

- tunnistaako minimax-algoritmi voiton selvästi voittavasta pelitilanteesta.

#### test_minimax_tie_over_loss

- valitseeko minimax-algoritmi tasapelin häviön sijasta pelin viimeisellä siirrolla.

#### test_minimax_win_over_tie

- valitseeko minimax-algoritmi voiton tasapelin sijasta pelin viimeisellä siirrolla.

## Kattavuusraportti

![image](https://github.com/user-attachments/assets/ffac1575-8599-46da-b4a5-a6559ee12934)


## Empiiriset testit

Empiiristen testien tavoitteena on testata valittua heuristiikkaa, eli pelaako tekoäly Black Hole-peliä optimaalisesti. Suoritin kaksi isompaa empiiristä koetta: ensimmäisessä kokeessa tekoäly pelasi toista tekoälyä vastaan, joka valitsee siirtonsa täysin satunnaisesti, ja toisessa kokeessa tekoäly pelasi toista tekoälyä vastaan, joka valitsee neljä ensimmäistä siirtoa täysin satunnaisesti. Kummassakin kokeessa pelataan 100 peliä ja lasketaan kummankin osapuolen voitot sekä tasapelit.
