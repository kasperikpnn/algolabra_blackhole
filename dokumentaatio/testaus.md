# Testausdokumentti

## Yleinen kuvaus

Projektin yksikkötestaus on toteutettu pytestillä. Yksikkötestien lisäksi projektia on testattu empiirisesti.

## Yksikkötestit

Tekoälylle on toteutettu yksikkötestit. Pelille ja sen käyttöliittymälle ei ole toteutettu testejä. Alla on jokainen testi järjestyksessä ja kategorioituna, ja lyhyt kuvaus testin tarkoituksesta.

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

Kattavuus on testattu coverage-työkalulla, jolla on luotu alla näkyvä raportti. 

(![image](https://github.com/user-attachments/assets/20aa5f00-8016-4937-a966-7bd18cdfcbf2)


## Testien toistaminen

Testauksen ohjeet löytyvät [käyttöohjeesta](https://github.com/kasperikpnn/algolabra_blackhole/blob/main/dokumentaatio/kayttoohje.md). Kattavuusreportin voi generoida seuraavilla komennoilla:

```
coverage run --branch -m pytest
coverage report -m
coverage html
```

Jonka jälkeen HTML-pohjaisen raportin voi löytää sijainnista /htmlcov/index.html.

## Empiiriset testit

Empiiristen testien tavoitteena on testata valittua heuristiikkaa, eli pelaako tekoäly Black Hole-peliä optimaalisesti.

Suoritin kaksi isompaa empiiristä koetta vanhalla heuristiikalla: ensimmäisessä kokeessa tekoäly pelasi toista tekoälyä vastaan, joka valitsee siirtonsa täysin satunnaisesti, ja toisessa kokeessa tekoäly pelasi toista tekoälyä vastaan, joka valitsee neljä ensimmäistä siirtoa täysin satunnaisesti. Kummassakin kokeessa pelataan 100 peliä ja lasketaan kummankin osapuolen voitot sekä tasapelit. Kokeet on suoritettu eri Python-tiedostossa, jossa pelin koodia on muokattu niin, että pelaajan syötteen sijasta tekoäly tekee kummatkin siirrot.

Suoritin uudella heuristiikalla toisen kokeen uudestaan (tekoäly pelaa toista tekoälyä vastaan, joka valitsee neljä ensimmäistä siirtoa täysin satunnaisesti). Testien perusteella vaikuttaa siltä, että uusi heuristiikka on alkupelissä hieman pätevämpi kuin vanha. Uudesta heuristiikasta löytyy selitys [toteutusdokumentista](https://github.com/kasperikpnn/algolabra_blackhole/blob/main/dokumentaatio/toteutus.md).

Testeissä pelin aloittava pelaaja valittiin satunnaisesti, joten jos pelissä jommallakummalla pelaajalla on etu, tätä ei ole otettu huomioon.

Tekoälyn vanha heuristiikka käytti tätä kaavaa saadakseen arvon:

> 2a + b - c - 2d

a = tyhjät ruudut, joissa vastapelaajalla on suurempi summa kuin tekoälyllä ja summien erotus on suurempi kuin tekoälyn seuraava numero

b = tyhjät ruudut, joissa vastapelaajalla on suurempi summa kuin tekoälyllä (sisältää siis myös a:n tyhjät ruudut)

c = tyhjät ruudut, joissa tekoälyllä on suurempi summa kuin vastapelaajalla

d = tyhjät ruudut, joissa tekoälyllä on suurempi summa kuin vastapelaajalla ja summien erotus on suurempi kuin vastapelaajan seuraava numero

Vanhan heuristiikan tekoäly täysin satunnaisia siirtoja vastaan:

![pie-chart](https://github.com/user-attachments/assets/f40a5042-81d6-46ac-8c08-ab7c7096573b)

Vanhan heuristiikan tekoäly toista tekoälyä vastaan, joka tekee neljä ensimmäistä siirtoa satunnaisesti:

![pie-chart (1)](https://github.com/user-attachments/assets/e1b0acc9-85dc-4bd7-aa15-fec1f29d6505)

Uuden heuristiikan tekoäly toista tekoälyä vastaan, joka tekee neljä ensimmäistä siirtoa satunnaisesti:

![pie-chart (2)](https://github.com/user-attachments/assets/58153f73-0834-44fc-93dc-d6ada4c58d2e)

