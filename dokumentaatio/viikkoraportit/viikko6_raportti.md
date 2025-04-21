# Viikko 6

## Maanantai
#### Käytetty aika: 3h

Kirjoitin käyttöohjeen ja jonkin verran toteutusdokumenttia. Toteutin myös symmetristen siirtojen poissulkemisen, mutta lopulta tästä olikin hyvin minimaalinen hyöty: symmetrisiä lautoja tuntuu löytyvän vain joko ensimmäisellä siirrolla tai harvemmin toisella siirrolla. Ensimmäisellä siirrolla päästään tämän toteutuksen jälkeen iteratiivisessa syvenemisessä yksi kerros syvemmälle. Saatan ottaa tämän pois koodista myöhemmin, sillä saavutettu hyöty tuntuu sen verran minimaaliselta.

## Keskiviikko
#### Käytetty aika: 3h

Aloin pohtimaan pelin alkupeliä: onko mahdollista löytää pelin alkuun jokin optimaalinen siirto, minkä tekoäly voisi aina tehdä, niin ettei sitä tarvitse laskea minimaxilla? Toteutin kopion pelistä, jossa tekoäly pelaa itseään vastaan. Tämä auttoi minua huomaamaan, että tekoäly pelaa tällä hetkellä alkupelin hyvin epäoptimaalisesti.

![image](https://github.com/user-attachments/assets/6769b6c1-2495-4a0e-bb17-ff51b8489871)

Tältä näyttää tällä hetkellä optimaalinen peli Black Holea tekoälylläni: se johtaa aina ensimmäisen pelaajan voittoon, jonka pelaaja tunnistaa joka kerta kuudennella vuorollaan. Tämä on kummallista, sillä alunperin uskoin, että toisella pelaajalla on tässä pelissä etu. Toinen pelaaja saa kuitenkin viimeisen siirron, joka on siirto millä on peliin huomattavasti eniten vaikutusta (saa päättää, kumpi ruuduista on Black Hole). Johtopäätökseni oli, että tekoälyn täytyy pelata tällä hetkellä alkupeliä epäoptimaalisesti. Ensimmäisissä siirroissa pelkästään ei tunnu olevan tällä hetkellä hirveästi logiikkaa: miksi paras siirto olisi ruutu 1? Luulen, että parhaan siirron täytyy olla joko jokin reunimmainen ruutu (saa vietyä omalla numerolla hyvän ruudun, jotta se ei jää toiselle pelaajalle), tai joku keskellä oleva ruutu (keskellä oleva ruutu todennäköisemmin päätyy mustaan aukkoon, ja sinne mielummin haluaa pieniä numeroita kuin isoja: realistisesti ei pysty välttämään sitä, etteikö jokin oma numero päätyisi mustaan aukkoon).

Muutin hieman kopiota pelistä niin, että toinen pelaaja valitseekin siirtonsa täysin sattumanvaraisesti ensimmäisellä neljällä vuorolla. Odotin, että toinen pelaaja onnistuisi sattumanvaraisella alkupelillä jossain vaiheessa voittamaan ensimmäisen pelaajan, jos tekoäly ei pelaa tällä hetkellä ensimmäisiä siirtoja optimaalisesti, ja näin kävikin.

![image](https://github.com/user-attachments/assets/9d409a15-ab86-4b7e-851c-495d234dc01c)

Toinen pelaaja sattumanvaraisesti kasasi omat alkupelin numeronsa reunalle ja kasaan, mikä osoittautui hyväksi strategiaksi. Ensimmäinen pelaaja teki mahdollisesti virheen kuudennella vuorollaan sijoittamalla oman numeronsa "keskelle" vapaaksi jäänyttä aluetta, jonka jälkeen toinen pelaaja löysi heti voiton. En osaa vielä oikein sanoa miksi, enkä osaa sanoittaa tätä vielä kunnolla, mutta tuntuu, että omat numerot kannattaa usein sijoittaa tyhjäksi jääneen alueen reunoille, ja harvemmin kannattaa "jakaa" tyhjäksi jäänyttä aluetta useaan osaan, niin kuin nyt ensimmäinen pelaaja teki siirrollaan. Yritän miettiä tätä tarkemmin ja mahdollisesti perustella tätä matemaattisesti.

## Torstai
#### Käytetty aika: 3h

Kokeilin uutta heuristiikkaa toivoen, että tekoälyn alkupeli kehittyisi parempaan suuntaan. Ideana oli, että kaikista häviävistä ruuduista ei tulisi rankaista tasapuolisesti: joskus häviävä ruutu, joka on jo täysin ympäröity numeroilla on oikeastaan paljon vähemmän paha kun häviävä ruutu, jonka täyttäminen lisää pelaajalle yhden tai useamman häviävän ruudun. Tämä pätee myös toiseen suuntaan: voittava ruutu on vahvempi silloin, jos vastapelaaja saa lisää häviäviä ruutuja täyttäessään sen. Uusi heuristiikka oli tämänkaltainen:
- voittava ruutu +1
- jos vastustaja täyttää tämän voittavan ruudun ja se aiheuttaa lisää voittavia ruutuja (häviäviä vastustajalle): +3 (kokeilin eri lukuja tässä)
- häviävä ruutu -1
- jos tekoäly täyttää tämän ruudun ja se aiheuttaa lisää häviäviä ruutuja tekoälylle: -3

Valitettavasti heuristiikka oli melko hidas ja testasin tätäkin heuristiikkaa laittamalla kaksi tekoälyä pelaamaan vastakkain niin, että toinen pelaaja pelasi ensimmäiset siirtonsa täysin sattumanvaraisesti, enkä saanut parempaa tulosta: toinen pelaaja onnistui välillä voittamaan myös sattumanvaraisilla siirroilla.

Pohdin myös, voiko voiton jo suoraan nähdä voittavien ja häviävien ruutujen määrästä, mutta joissain pelilaudan tilanteissa, erityisesti keskivaiheissa peliä tämä tuntuu haastavalta. Yritän miettiä tätä pidemmälle.

## Perjantai
#### Käytetty aika: 3h

Aika meni lähinnä taas uuden heuristiikan miettimiseen ja eri arvojen kokeiluun, mutta mikään ei oikein tuntunut tuottavan tulosta. Tehostin hieman algoritmia toteuttamalla summataulukon (laskee summat tyhjien ruutujen ympärillä ja taulukkoa ylläpidetään joka siirron jälkeen), jota käytetään heuristiikkaa laskiessa.

Ylläpidän myös listaa jokaisen tyhjän ruudun naapureiden määrästä, ja järjestän siirrot näin: ensin kokeillaan sitä ruutua jolla on vähiten naapureita, sitten ruutua jolla on eniten naapureita, sitten ruutua jolla on toiseksi vähiten naapureita ja niin edelleen. Uskon, että paras siirto on yleensä jompikumpi: joko halutaan minimoida oman siirron vaikutus laudalle, tai sitten halutaan laittaa oma numero mahdollisimman keskelle. Ehkä tämä ei tosin ole paras tapa järjestää siirrot: ne voitaisin järjestää vaikka esimerkiksi omien summien mukaan, yleensä omat siirrot tehdään niihin ruutuihin, jotka ovat sillä hetkellä pelaajalle häviäviä. Oma vuorohan kuitenkin on oikeastaan aina itselle nettonegatiivinen, ja ainoa omaa peliä edistävä asia mitä voidaan tehdä on häviävien ruutujen peittäminen.

Aika alkaa loppua kesken, niin minun täytyy varmaan alkaa vihdoin toteuttamaan testejä ja kirjoittaa toteutusdokumentti loppuun ennen kuin jatkan tekoälyn kehittämistä, vaikka sen osalta olisikin vielä paljon ideoita. Olisi ollut hyvä käydä keskustelua ohjaajan kanssa, ehkä sen vielä ehtii tehdä ennen lopullista palautusta.
