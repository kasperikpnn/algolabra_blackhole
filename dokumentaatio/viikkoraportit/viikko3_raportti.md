# Viikko 3

## Torstai
#### Käytetty aika: 5h

Hyvin produktiivinen päivä! Sain hyviä vinkkejä ohjaajalta, miten lähteä toteuttamaan tekoälyä. Kehitin ensin voiton tunnistuksen, ja lähdin sen jälkeen toteuttamaan minimaxia ja iteratiivista syvenemistä yhtä aikaa. Ymmärtääkseni minimax-algoritmiä, alpha-beta -karsintaa paremmin, tutkin ensin muutamia esimerkkejä, joista eniten auttoi [Keith Gallin Connect 4-tekoälyn toteutus.](https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py) Tämän jälkeen kyselin ChatGPT:ltä iteratiivisesta syvenemisestä. Myöhemmin lisäsin myös samassa pelitilanteessa parhaaksi osoittautuneen siirron muistamisen seuraavissa iteraatioissa.

Heuristiikkana käytän tällä hetkellä arvoa (tekoälyn senhetkisten voittoruutujen määrä - tekoälyn senhetkisten häviävien ruutujen määrä). Se ei mielestäni ole kaikista optimaalisin, mutta vaikuttaa toimivan toivotusti: tekoäly välttelee keskimmäisiä ruutuja kovasti alkupelissä, koska sillä hetkellä ne luovat enemmän häviäviä ruutuja tekoälylle. Tämä johtaa suoraan siihen, että tekoäly kasaa omat numeronsa lähelle toisiaan alkupelissä (vasempaan yläreunaan pelilautaa), mikä toki on mielestäni tärkeä strategia pelissä.

Onnistuin pelaamaan yhden tasapelin tekoälyä vastaan (kaduttaa, etten tallentanut kyseistä peliä itselleni muistiin, se olisi varmasti ollut tärkeää dataa), mutta muuten tekoäly voittaa minut melko usein. Yritän kehittää huomenna tekoälylle lisää testejä, tällä hetkellä testit käyvät läpi vain evaluate-funktion. *Muokkaus: Onnistuin saavuttamaan voiton myöhemmin tekoälyä vastaan, ja otin lopullisen pelitilanteen talteen.*

Yksi idea, mikä minulla on jatkokehitystä varten, on symmetristen pelitilanteiden käsitteleminen vain kerran. En tosin tiedä vielä, miten tämä kannattaisi toteuttaa järkevästi (tai hidastaako epäsymmetriset pelitilanteet edes tekoälyn toimintaa yhtään merkittävästi).

## Perjantai & lauantai
#### Käytetty aika: 2h

Korjasin erittäin ison bugin. Minimaxissa jokainen, eli myös pelaajan siirrot nähtiin tekoälyn liikkeenä, mikä johti siihen että tekoäly pelasi erityisesti loppupelin hyvin epäoptimaalisesti. Nyt tekoäly voittaa minut pelissä aina ja ilmeisesti pystyy laskemaan aina voiton itselleen loppupelissä, joskus ilmeisesti jopa viidennen siirron jälkeen. (ainakin tekoäly antaa siirrolle arvon inf)

En ole enää varma, onko heuristiikka tästä kehitettävissä: nykyisellä heuristiikalla tekoäly pelaakin peliä huomattavasti paremmin kuin odotin. Omien numeroiden "muuraaminen" pienempien numeroiden taakse ei toimi, sillä tekoäly tajuaa parhaan siirron jossain kohtaa olevan omien numeroiden sijoittaminen "muurini" taakse. Ehkä alkuperäinen oletukseni (pienet numerot kannattaa sijoittaa mahdollisimman keskelle) olikin väärä: se, että tekoäly vie jo alussa yhden pyramidin nurkista omalla ykkösellään saattaakin olla edullista, sillä nurkat ovat todella hyviä positioita omille numeroille ja tällöin vastapelaajalla on yksi nurkka vähemmän käytettävissä.

En ole myöskään ihan varma, minkälaisia testejä minun kannattaisi kehittää minimaxille, niin en oikein vielä saanut mitään aikaan. Pitäisi varmaankin miettiä eri pelitilanteita, joissa on jokin hyvin selkeä voittoon johtava liike, joka tekoälyn täytyy tunnistaa, ja syöttää nämä minimaxille/iteratiivisen syvenemisen funktiolle odottaen tiettyä vastausta.

Kyselen ensi viikolla mahdollisesti Zoom-aikaa tai vain Telegram-ohjausta jos saisin sitä kautta ohjaajalta lisäkehitysideoita.
