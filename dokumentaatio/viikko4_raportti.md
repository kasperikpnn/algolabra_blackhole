# Viikko 4

## Torstai
#### Käytetty aika: 2h

Aika käytetty lähinnä ohjaajan kanssa tapaamiseen. Sain paljon ideoita, miten nopeuttaa tekoälyn koodia: esimerkiksi vähentämällä turhia funktiokutsuja ja ylläpitämällä jokaisen ruudun senhetkistä summaa. Myös mahdolliset siirrot voisi järjestää heuristiikan mukaan.

## Perjantai ja lauantai
#### Käytetty aika: 2h

En ehtinyt valitettavasti tällä viikolla käyttää hirveästi aikaa työhön muiden kiireiden takia. Toteutin aiemmin muutokset, mutta koodi ei nopeutunut oikeastaan ollenkaan ja alkoi tekemään aiemmasta koodista eroavia päätöksiä oudoilla heuristiikan arvoilla, joten koodin täytyy olla jotenkin viallinen.

Aloitin muokkausten tekemisen vielä uudemman kerran, palauttamalla koodin ennalleen ja tekemällä ne muutokset jotka eivät ole merkittävän isoja (pelaajien numeroiden ylläpitäminen int-arvoina minimaxissa listan sijasta, tyhjien ruutujen listan lähettäminen eteenpäin minimaxissa uuden listan luomisen sijaan, evaluate-funktion kehittäminen (ei kutsu enää compute_scores funktiota). Näillä muutoksilla ei päästy vielä syvempiin iteraatioihin ainakaan ensimmäisillä siirroilla, kuin aiemmalla koodilla. Tämä koodi sijaitsee nyt blackhole_ai.py tiedostossa ja aiemmin toteutettu mahdollisesti buginen koodi, mutta jossa on ainakin teoriassa enemmän isoja nopeutuksia on blackhole_ai_new.py tiedostossa.

Ensi viikolla aion panostaa koodiin enemmän, sekä myös aloittaa testausdokumentin ja toteutusdokumentin tekemisen. Myös testejä täytyisi lisätä, olen niiden osalta pahasti jäljessä. (nykyinen yksittäinen testi ei välttämättä edes toimi oikein uuden evaluate-funktion kanssa)

