# Toteutusdokumentti

## Yleisrakenne

Black Hole-harjoitustyö koostuu kahdesta osasta: tekoälystä (blackhole_ai.py) ja pelistä (blackhole_game.py). Tämä dokumentti keskittyy tekoälyn toteutukseen, mutta myös pelin toteutuksesta kerrotaan lyhyesti.

### Pelin toteutus

Peli itse on toteutettu niin, että pelilauta tallennetaan listana, joka sisältää jokaisen pelilaudan ruudun sisällön. Jos ruutu on tyhjä, sen arvo on None, ja jos ruudussa on vaikka tekoälyn sijoittama numero 5, sen arvo on tuple ("AI", 5). Peli on käytännössä 20 kertaa itseään toistava osa koodia, jossa vaihdetaan joka kerta vuoroa pelaajan ja tekoälyn välillä ja kasvatetaan juuri pelanneen pelaajan seuraavaa numeroa, kunnes kummatkin pelaajat ovat pelanneet luvun 10 ja yksi ruutu jää jäljelle.

Jokaisen ruudun vierekkäiset ruudut ovat tallennettuna adjacency-sanakirjaan, jonka avain on ruutu itse ja arvona on vierekkäiset ruudut. Tätä sanakirjaa tekoäly käyttää arvioidessaan pelitilannetta, sekä peli käyttää tätä sanakirjaa pelin lopussa laskiessaan pelaajien summan mustan aukon ympärillä.

### Tekoälyn toteutus

Tekoäly saa alkuun tiedon nykyisestä pelilaudasta ja kummankin pelaajan seuraavasta numerosta. Tämän jälkeen tekoäly tekee listan mahdollisista jäljellä olevista siirroista. Nämä tiedot laitetaan eteenpäin metodille iterative_deepening, joka toteuttaa tekoälylle nimensä mukaan iteratiivisen syvenemisen. Tämä tarkoittaa sitä, että pelipuun tiloja tutkitaan jatkuvasti kasvavalla rajalla: ensin siis tehdään haku parhaalle siirrolle, joka löytyy kun mennään yhden siirron päähän, sen jälkeen tehdään uudestaan haku, mutta mennään pelipuussa kahden siirron päähän. Syvyyttä kasvatetaan kunnes aikaraja saavutetaan. Aikaraja on "pehmeä" aikaraja, eli tekoäly voi vielä aloittaa uuden haun vaikka mennyt aika ja uuteen hakuun menevä aika olisi pidempi kuin annettu aikaraja.

Tekoäly suorittaa haun parhaalle siirrolle minimax-algoritmilla, jolla yritetään maksimoida heuristinen arvo ottaen huomioon, että toinen pelaaja pelaa optimaalisesti ja minimoi tekoälyn arvon. Algoritmi käyttää myös alpha-beta -karsintaa, joka karsii tutkittavia pelipuun haaroja: jos huomataan esimerkiksi, että jokin siirto takaisi vastapelaajalle voiton, niin tätä haaraa ei tarvitse tutkia pidemmälle. Tekoäly myös järjestää siirtoja kahdella eri tavalla: ensin järjestetään mahdolliset siirrot jokaisen ruudun naapurien määrän mukaan (ruutua, jolla on vähiten naapureita, kokeillaan ensin mahdollisena siirtona), ja tämän jälkeen etsitään best_moves-sanakirjasta viimeksi samassa pelitilanteessa parhaaksi havaittu siirto ja nostetaan se ensimmäiseksi kokeiltavaksi siirroksi.

### Heuristiikka

Tekoäly saa heuristisen arvonsa tällä kaavalla:

> 2a + b - c - 2d

Missä:
a = tyhjät ruudut, joissa vastapelaajalla on suurempi summa kuin tekoälyllä ja summien erotus on suurempi kuin tekoälyn seuraava numero
b = tyhjät ruudut, joissa vastapelaajalla on suurempi summa kuin tekoälyllä (sisältää siis myös a:n tyhjät ruudut)
c = tyhjät ruudut, joissa tekoälyllä on suurempi summa kuin vastapelaajalla
d = tyhjät ruudut, joissa tekoälyllä on suurempi summa kuin vastapelaajalla ja summien erotus on suurempi kuin vastapelaajan seuraava numero

## Tila- ja aikavaativuudet

Naiivin minimax-algoritmin aikavaativuus on O(b^d), jossa b on *branching factor* eli mahdollisten siirtojen määrä ja d on *depth* eli syvyys. Black Holessa b on aina <= 21.

Alpha-beta -karsinnalla ja siirtojen järjestämisellä tehostettu minimax-algoritmi voi parhaassa tapauksessa saavuttaa aikavaativuuden O(b^(d/2), jos alpha-beta -katkaisu tapahtuu aina ensimmäisellä kokeillulla siirrolla. Pahimmassa tapauksessa aikavaativuus on edelleen O(b^d), jos yhtäkään alpha-beta -katkaisua ei tapahdu.

Algoritmin tilavaativuus on O(bd) + parhaiden siirtojen muistamiseen vaadittava välimuisti.

Muiden tekoälyn käyttämien metodien, kuten *obtain_info* (tehdään ennen minimaxiin siirtymistä) ja *evaluate* (annetaan laudalle heuristinen arvo) aikavaativuudet ovat O(1).

## Puutteet ja parannusehdotukset

### Puutteet

- Algoritmin käyttämä heuristiikka ei ole optimaalinen erityisesti alkupelissä empiirisen testauksen perusteella, jossa tekoäly pelaa itseään vastaan, mutta toinen tekoälyistä tekee ensimmäiset neljä siirtoa täysin satunnaisesti. Alkupelin satunnaisesti pelaava tekoäly onnistuu monestikin voittamaan täysin heuristiikkapohjaisesti pelaavan tekoälyn: valitettavasti tästä ei ole dataa, mutta arvio on että noin 10% ajasta satunnaisesti pelattu alkupeli voittaa heuristiikkapohjaisen alkupelin.

### Parannusehdotukset

- Tekoälyn heuristiikkaa voisi kehittää. Todennäköisesti on mahdollista havaita laskelmallisesti voittava pelitilanne jo ennen viimeistä siirtoa, mikä tekisi tekoälystä tehokkaamman jo pelin alkupuolella. Nykyisellä toteutuksella tekoäly löytää voittavan/häviävän tilanteen yleensä vasta kuudennella siirrollaan, jolloin se ehtii analysoimaan pelin loppuun asti.
- Black Hole-peliä itsessään täytyisi analysoida tarkemmin tekoälyn jatkokehitystä varten. Onko ensimmäisellä vai toisella pelaajalla Black Holessa etu? Onko pelin alussa jokin objektiivisesti paras siirto, joka voidaan tehdä aina ilman minimaxia? Onko jokin toinen tapa analysoida pelilaudan tämänhetkistä tilannetta parempi, kuin tyhjien ruutujen summien laskeminen? Onko paras strategia alkupelissä sittenkään asettaa omat numerot ruutuihin, joissa on mahdollisimman vähän naapureita vai onko pienien numeroiden asettaminen laajemmin parempi idea?
- Tekoälyn jatkokehitystä varten voisi olla hyödyllistä tallentaa jokainen pelattu peli ja jokainen tekoälyn siirrolle saama arvo tekstimuotoisesti, ja sen lopputulos.
- Pelillä voisi olla graafinen käyttöliittymä, tai se voisi vähintään olla jollain tapaa selkeämpi. Joillekin uusille pelaajille oli vaikeaa hahmottaa mitkä ruudut ovat vierekkäisiä.
- Pelaajien luvut voitaisiin erottaa toisistaan kompaktimmin esimerkiksi väreillä: kokeilin tämän ratkaisemiksi alkuun *coloramaa*, mutta päätin lopulta olla käyttämättä sitä, koska en ollut varma olisiko se yhteensopiva kaikkien käyttöjärjestelmien terminalien kanssa.

## Laajojen kielimallien käyttö

Olen käyttänyt ChatGPT-4o (OpenAI)-kielimallia näihin asioihin:
- itse pelin koodin kehittämisen tukena: pyysin tekoälyä suoraan kehittämään pelille koodin, ja sain osittain toimivaa koodia josta käytin suoraan joitain hyviä ideoita
- itselleni uusien konseptien (minimax-algoritmi, iteratiivinen syveneminen, alpha-beta -karsinta) selittämiseen esimerkkien avulla
- virheanalyysiin monissa eri tilanteissa, missä ohjelman toiminta on keskeytynyt virheen vuoksi

## Lähteet

- [Wikipedia: Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Wikipedia: Minimax](https://en.wikipedia.org/wiki/Minimax)
- [Locall.host: Mastering the Complexity: Unraveling the Minimax Algorithm’s Difficulty](https://locall.host/is-minimax-algorithm-hard/)
