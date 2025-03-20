# Viikko 2

Tästä viikosta lähtien kirjoitan aina viikkoraporttiin jotain jokaisen päivän päätteeksi, milloin olen työstänyt harjoitustyötä.

## Keskiviikko
#### Käytetty aika: 2h

Käytetty aika meni lähinnä ajatustyöhön: en saanut ollenkaan koodia kirjoitettua. Pohdin pääasiassa, miten itse peli kannattaa toteuttaa. Peli itsessään pitäisi vaatia aika vähän koodia, ja toteutuksen pitäisi olla mahdollista vain yhdessä päivässä. Isoja kysymyksiä mielessäni toteutuksen osalta olivat esimerkiksi se, kannattaako ruudut toteuttaa olioina joille määritellään mm. viereiset ruudut (jos ruutu jää pelin lopussa tyhjäksi ja muuttuu mustaksi aukoksi), sekä niiden sisältämä numero ja sen asettama pelaaja. Pohdin myös, miten on mahdollista erottaa pelaajien numerot toisistaan tekstipohjaisessa terminal-ympäristössä. Tutustuin esimerkiksi [coloramaan](https://pypi.org/project/colorama/), joka mahdollistaa värillisen tekstin terminalissa. Olen kuitenkin epävarma, että toimiiko colorama eri ympäristöissä toivotusti, ja päätin olla käyttämättä sitä harjoitustyössäni, ainakin toistaiseksi. Tärkeämpää on kuitenkin päästä pelin tekoälyn toteutukseen.

Tekoälyn toteutusta mietin myös hieman, ja pohdin, mikä olisi paras tapa kuvata pelitilannetta parhaan siirron arvioimiseksi. Yksinkertaisin tapa olisi laskea sen hetkisten tyhjien ruutujen, eli mahdollisten mustien aukkojen summat kummallekkin pelaajalle yhteen: se pelaaja, jolla on sillä hetkellä vähemmän häviäviä mustia aukkoja, on johtoasemassa. Mutta onko tilanne oikeasti niin huono, vaikka pelaajalla olisi useampikin häviävä musta aukko? Ainakin pelin alussa uskoisin, että optimaalinen liike on sijoittaa pienet luvut mahdollisimman keskelle lautaa niin, että niitä ympäröi mahdollisimman moni ruutu, sillä isommat numerot saa täten helpommin parempiin positioihin. Tämä yksinkertainen pelitilanteen arviointi sotisi siis täysin omaa intuitiotani vastaan, ainakin ihan pelin alussa.
