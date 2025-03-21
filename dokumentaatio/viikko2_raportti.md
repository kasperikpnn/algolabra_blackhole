# Viikko 2

Tästä viikosta lähtien kirjoitan aina viikkoraporttiin jotain jokaisen päivän päätteeksi, milloin olen työstänyt harjoitustyötä.

## Keskiviikko
#### Käytetty aika: 2h

Käytetty aika meni lähinnä ajatustyöhön: en saanut ollenkaan koodia kirjoitettua. Pohdin pääasiassa, miten itse peli kannattaa toteuttaa. Peli itsessään pitäisi vaatia aika vähän koodia, ja toteutuksen pitäisi olla mahdollista vain yhdessä päivässä. Isoja kysymyksiä mielessäni toteutuksen osalta olivat esimerkiksi se, kannattaako ruudut toteuttaa olioina joille määritellään mm. viereiset ruudut (jos ruutu jää pelin lopussa tyhjäksi ja muuttuu mustaksi aukoksi), sekä niiden sisältämä numero ja sen asettama pelaaja. Pohdin myös, miten on mahdollista erottaa pelaajien numerot toisistaan tekstipohjaisessa terminal-ympäristössä. Tutustuin esimerkiksi [coloramaan](https://pypi.org/project/colorama/), joka mahdollistaa värillisen tekstin terminalissa. Olen kuitenkin epävarma, että toimiiko colorama eri ympäristöissä toivotusti, ja päätin olla käyttämättä sitä harjoitustyössäni, ainakin toistaiseksi. Tärkeämpää on kuitenkin päästä pelin tekoälyn toteutukseen.

Tekoälyn toteutusta mietin myös hieman, ja pohdin, mikä olisi paras tapa kuvata pelitilannetta parhaan siirron arvioimiseksi. Yksinkertaisin tapa olisi laskea sen hetkisten tyhjien ruutujen, eli mahdollisten mustien aukkojen summat kummallekkin pelaajalle yhteen: se pelaaja, jolla on sillä hetkellä vähemmän häviäviä mustia aukkoja, on johtoasemassa. Mutta onko tilanne oikeasti niin huono, vaikka pelaajalla olisi useampikin häviävä musta aukko? Ainakin pelin alussa uskoisin, että optimaalinen liike on sijoittaa pienet luvut mahdollisimman keskelle lautaa niin, että niitä ympäröi mahdollisimman moni ruutu, sillä isommat numerot saa täten helpommin parempiin positioihin. Tämä yksinkertainen pelitilanteen arviointi sotisi siis täysin omaa intuitiotani vastaan, ainakin ihan pelin alussa.

## Torstai
#### Käytetty aika: 3h

Käytetty aika meni taas suurimmaksi osaksi ajatustyöhön, mutta sain myös jonkin verran koodiakin kirjoitettua. Kysyin ChatGPT:ltä, miten tämä toteuttaisi pelille koodin ja saamani koodi oli osittain rikkinäistä ja virheellistä, mutta otin toteutuksesta hieman inspiraatiota: laudan tallentaminen 2D-taulukkona ja vierekkäisten ruutujen tallentaminen dictionary-muodossa tuntuu yksinkertaisimmalta tavalta toteuttaa peli olio-ohjelmoinnin sijasta. 2D-taulukkona laudan tilanne on myös helppoa antaa tekoälylle käsiteltäväksi.

Pelasin myös tyttöystäväni kanssa yhden Black Hole-pelin, joka sai minut oivaltamaan sen, että aiemmin pohtimani yksinkertainen toteutus pelitilanteen analysoimiseksi ei ole paras. Joissain pelitilanteissa, erityisesti loppupuolella peliä parasta on se, että "autat" toista pelaajaa ja täytät hänelle sillä hetkellä häviävän mustan aukon, erityisesti jos tämä musta aukko on jo täysin ympäröity luvuilla, sillä saat silloin oman ison lukusi "piiloon".

## Perjantai
#### Käytetty aika: 3h

Käytetty aika meni kokonaan pelin ja sen käyttöliittymän toteutukseen. Olen tyytyväinen toteutukseen: päämääränä oli itse toteutuksen lisäksi ohjelmoida peli niin, että tekoälyn on helppo saada pelitilanteesta dataa. Lauta tallennetaan 2D-taulukkona, jossa jokainen ruutu on aluksi None-tyyppinen, ja ruudun täytyttyä se sisältää numeron ja sen pelanneen pelaajan (pelaaja ("P1") tai tekoäly ("AI")). Pelaajien jäljellä olevista numeroista en ole varma, miten ne kannattaa tallentaa käsittelyä varten, mutta uskoisin että tiedon niistä voi saada pelkästä vuoronumerosta. (jos on tekoälyn vuoro ja on meneillään 7. vuoro, niin se yksin antaa tiedon, että tekoäly on pelin aloittanut pelaaja ja luvut 4-10 ovat vielä pelaamatta). Tämänhetkinen tekoäly tekee vuoron täysin satunnaisesti johonkin tyhjään ruutuun, sillä tarkoituksenani oli vain toistaiseksi saada peli pelattavaan muotoon.

