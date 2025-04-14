# Määrittelydokumentti

Tämä dokumentti määrittelee Helsingin Yliopiston tietojenkäsittelytieteen kandiohjelman kevään 2025 3. periodin Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssin laboratoriotyötoteutuksen. Opinto-ohjelmani on tietojenkäsittelytieteen kandiohjelma.

## Aihe

Harjoitustyön aiheen ydin on toteuttaa tekoäly Black Hole-pelille. Tekoäly toteutetaan todennäköisesti minimax-algoritmilla, jota on tehostettu alpha-beta-karsinnalla sekä optimoinnilla käyttäen iteratiivista syvenemistä, ja siirtojen järjestämistä edellisen iteraation perusteella. Tavoitteena on, että tekoäly pystyy pelaamaan ihmistä vastaan, eli myös sovelluslogiikka ja käyttöliittymä pelille täytyy toteuttaa. Käyttöliittymä tulee hyvin todennäköisesti olemaan tekstipohjainen.

Työ toteutetaan Python-ohjelmointikielellä. Vertaisarviointia varten ymmärrän myös tarvittaessa Javaa.

### Peli

Tutustuin itse peliin [Tom Scottin videolta](https://www.youtube.com/watch?v=zMLE7a3faI4), minkä katsominen on yksi tapa hahmottaa pelin kulkua.

Black Hole on kynä- ja paperipeli. Black Hole-"lauta" muodostuu paperille piirtämällä palloista muodostuva kolmio tähän tapaan:
```
        ()
       ()()
      ()()()
     ()()()()
    ()()()()()
   ()()()()()()
```
Nyt pelaajat asettavat kolmion ruutuihin lukuja vuorotellen, aloittaen luvusta 1, jonka jälkeen asetetaan luku 2, 3, ..., päättyen siihen, että kumpikin pelaaja asettaa omalla vuorollaan luvun 10. Kolmioon jää lopulta yksi tyhjä ruutu, joka on ns. "musta aukko", joka imee ympärillään olevat numerot. Lasketaan kummankin pelaajan luvut yhteen, jotka olivat mustan aukon ympärillä. Voittaja on se pelaaja, jonka yhteenlaskettu summa on pienempi. Jos summat ovat yhtä suuria, peli päättyy tasapeliin. (peliin voisi keksiä säännön, jolla ratkaista tasapelitilanne, mutta tässä toteutuksessa tasapelejä ei ratkaista)

## Dokumentaatio

Kaikki dokumentaatio laboratoriotyötä koskien on kirjoitettu suomeksi. Ohjelmassa muuttujat yms. saattavat olla nimettynä englanniksi, mutta koodin kommentointi kirjoitetaan myös suomen kielellä.
