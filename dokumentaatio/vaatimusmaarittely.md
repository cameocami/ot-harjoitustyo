# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi luoda itselleen kauppalistan ruokakaupan tuotteista. 


## Käyttöliittymäluonnos

Käyttöliittymä koostuu yhdestä näkymästä, johon sovellus aukeaa, kun se käynnistetään. Kyseinen näkymä sisältää kaikki sovelluksen toiminnalisuudet. (tehty)


![](./kuvat/kayttoliittyma-hahmotelma.png)

Sovelluksen käyttöliittymän lisäksi sovellus luo html-tiedostoja valmiista kauppalistoista. Nämä tallentuvat paikallisesti sovelluksen kansioon.


## Perusversion tarjoama toiminnallisuus

### Tuotteen lisääminen kauppalistalle (tehty)

Käyttäjä kirjoittaa kirjoituskenttään haluamansa tuotteen ja määrän, sekä valitsee pudotusvalikosta määräyksikön. (tehty) Jos kyseinen on tuote on sovelluksen tuotetietokannassa, valitsee sovellus tuotteelle sille määritellyn osaston. (tehty) Jos tuote ei löydy sovelluksen tuotetietokannasta, käyttäjän valitsee tuottelle osaston. (tehty)

Käyttäjä lisää tuotteen kauppalistalle painamalla "lisää"-painiketta. (tehty) Mikäli tuotetta ei löytynyt sovelluksen tuotetietokannasta, lisätään tuotteen nimi ja sen osasto myös tuotetietokantaan. (tehty) Mikäli tuote on jo kauppalistalla, tuotteen lisääminen kasvattaa tuotteen määrää. (tehty)

### Tuotteiden hallinointi kauppalistalla

Kun tuotteita on lisätty kauppalistalle, voi käyttäjä vielä muokata haluttua määrää. Painamalla "-" tai "+" -painikkeita, käyttäjä pystyy vähentämään tai lisäämään haluttua tuotteen määrää. Painamalla "poista"-painiketta, käyttäjä voi poistaa tuotteen kauppalistalta. 

### Kauppalista tiedosto kokoaminen

Kun käyttäjä on valmis kauppalistan kanssa, "laadi kauppalista"-painike kokoaa listan tuotteet html-tiedostoon. (osin tehty, tiedosto toteutettu txt-tiedostona)

## Jatkokehitysideoita

Perusversion jälkeen sovellusta voidaan täydentää esim. seuraavilla toiminnallisuuksilla, mikäli aika sallii:

- Kauppalistan tyhjennys - käyttäjä voi poistaa kaikki tuotteet kauppalistalta.
- Kauppalistan järjestely - käyttäjä voi valita minkä perusteella tuotteet järjestellään kauppalistaan.
- Oikoluku - Sovellus ehdottaa tuotetietokannasta löytyvää tuotteen nimeä, jos kirjoitettu tuotteen nimi on muutaman kirjaimen päässä tietokannasta löytyvästä nimestä. (tehty)
- Osastojen järjestely mahdollisuus - käyttäjä voi järjestellä ruokakaupan osastot uuteen järjestykseen
- Suosikkituotteiden valinta - käyttäjä voi valita suosikkituotteensa tuotetietokannasta
- Reseptien luonti - Käyttäjä voi luoda reseptejä, jolla käyttäjä saa lisättyä kaikki reseptin ainesosat kauppalistalle
