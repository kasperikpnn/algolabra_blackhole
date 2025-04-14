# Toteutusdokumentti

Työn alla!

## Yleisrakenne

Black Hole-harjoitustyö koostuu kahdesta osasta: itse pelistä (blackhole_game.py) ja tekoälystä (blackhole_ai.py).

### Pelin toteutus

Peli itse on toteutettu niin, että pelilauta tallennetaan listana, joka sisältää jokaisen pelilaudan ruudun sisällön. Jos ruutu on tyhjä, sen arvo on None, ja jos ruudussa on vaikka tekoälyn sijoittama numero 5, sen arvo on tuple ("AI", 5). Peli on käytännössä 20 kertaa itseään toistava osa koodia, jossa vaihdetaan joka kerta vuoroa pelaajan ja tekoälyn välillä ja kasvatetaan juuri pelanneen pelaajan seuraavaa numeroa, kunnes kummatkin pelaajat ovat pelanneet luvun 10 ja yksi ruutu jää jäljelle.

Jokaisen ruudun vierekkäiset ruudut ovat tallennettuna adjacency-sanakirjaan, jonka avain on ruutu itse ja arvona on vierekkäiset ruudut. Tätä sanakirjaa tekoäly käyttää arvioidessaan pelitilannetta, sekä peli käyttää tätä sanakirjaa pelin lopussa laskiessaan pelaajien summan mustan aukon ympärillä.

### Tekoälyn toteutus

Tekoäly saa alkuun tiedon nykyisestä pelilaudasta ja kummankin pelaajan seuraavasta numerosta. Tämän jälkeen tekoäly tekee listan mahdollisista jäljellä olevista siirroista. Nämä tiedot laitetaan eteenpäin metodille iterative_deepening, joka toteuttaa tekoälylle nimensä mukaan iteratiivisen syvenemisen. Tämä tarkoittaa sitä, että pelipuun tiloja tutkitaan jatkuvasti kasvavalla rajalla: ensin siis tehdään haku parhaalle siirrolle, joka löytyy kun mennään yhden siirron päähän, sen jälkeen tehdään uudestaan haku, mutta mennään pelipuussa kahden siirron päähän. Syvyyttä kasvatetaan kunnes aikaraja saavutetaan. Aikaraja on "pehmeä" aikaraja, eli tekoäly voi vielä aloittaa uuden haun vaikka mennyt aika ja uuteen hakuun menevä aika olisi pidempi kuin annettu aikaraja.

Tekoäly suorittaa haun parhaalle siirrolle minimax-algoritmilla, jolla yritetään maksimoida siis oma heuristiikka-arvo ottaen huomioon, että toinen pelaaja pelaa optimaalisesti ja minimoi tekoälyn arvon. Algoritmi käyttää myös alpha-beta -karsintaa, joka karsii tutkittavia pelipuun haaroja: jos huomataan esimerkiksi, että jokin siirto takaisi vastapelaajalle voiton, niin tätä haaraa ei tarvitse tutkia pidemmälle. Tekoäly myös tallentaa best_moves-sanakirjaan itselleen muistiin viimeksi samassa pelitilanteessa parhaaksi havaitun siirron, ja järjestää tämän siirron tulevissa hauissa tutkittavissa siirroissa ensimmäiseksi, aiheuttaen enemmän alpha-beta -katkaisuja.

## Tila- ja aikavaativuudet

## Suorituskyky- ja O-analyysivertailu

## Puutteet ja parannusehdotukset

## Laajojen kielimallien käyttö

Olen käyttänyt ChatGPT-4o (OpenAI)-kielimallia näihin asioihin:
- itse pelin koodin kehittämisen tukena: pyysin tekoälyä suoraan kehittämään pelille koodin, ja sain osittain toimivaa koodia josta käytin suoraan joitain hyviä ideoita
- monien itselleni uusien konseptien (minimax-algoritmi, iteratiivinen syveneminen, ym.) selittämiseen esimerkkien avulla
- virheanalyysiin monissa eri tilanteissa, missä ohjelman toiminta on keskeytynyt virheen vuoksi

## Lähteet
