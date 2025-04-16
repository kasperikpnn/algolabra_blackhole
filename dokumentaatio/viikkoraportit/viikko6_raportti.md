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
