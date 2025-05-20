# Käyttöohje

## Kuvaus

Black Hole on peli, jota voi pelata tekstipohjaisessa käyttöliittymässä tekoälyä vastaan. Pelistä itsestään löytyy ohjeet määrittelydokumentissa, sekä pelin käynnistettäessä selitetään pelin kulku lyhyesti.

## Käyttöohje

1. Kloonaa repositorio komennolla $ git clone https://github.com/kasperikpnn/algolabra_blackhole.git
2. Vaihda repositorion juurihakemistoon terminalissa esimerkiksi cd-komennolla.

(huom. jos et suorita testejä, askeleet 3-4 ovat täysin valinnaisia, sillä peli itsessään ei käytä Pythonin vakiokirjaston ulkopuolisia kirjastoja)

3. Asenna riippuvuudet komennolla ```$ poetry install``` (tarvitset [Poetryn](https://python-poetry.org/docs/) tätä varten)
4. Aktivoi virtuaaliympäristö komennolla ```$ poetry shell```
5. Aloita ohjelma komennolla ```$ python3 src/blackhole_game.py```
6. Ohjelmaa voi nyt käyttää käyttöliittymän ohjeiden mukaisesti. Käytännössä syötät vain pelilaudan ruutujen sijaintinumeroita sijoittaaksesi siihen numeron, niin kauan kunnes peli päättyy.

## Testien käyttöohje
(seuraa aiempien käyttöohjeiden askelia 1-4, jos et ole sitä tehnyt)
1. Aloita testit komennolla ```$ pytest src```
