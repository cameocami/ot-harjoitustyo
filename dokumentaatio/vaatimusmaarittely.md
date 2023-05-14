# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi luoda kauppalistan haluamistaan ruokakaupan tuotteista. Valmis kauppalista, jossa tuotteet ovat osastoittain siinä järjestyksessä kun ne esiintyvät kaupassa tallentuu paikalliskansioon. Käyttäjä voi käyttää jo tietokannasta löytyviä tuotteita tai luoda uusia tuotteita kirjoittamalla niille nimen ja valitsemalla niille osaston.


## Käyttöliittymäluonnos

Käyttöliittymä koostuu yhdestä näkymästä, johon sovellus aukeaa, kun se käynnistetään. Kyseinen näkymä sisältää kaikki sovelluksen toiminnalisuudet.

![](./kuvat/kayttoliittyma-hahmotelma.png)

Sovelluksen käyttöliittymän lisäksi sovellus luo tekstitiedostoja kauppalistoista. Nämä tallentuvat paikallisesti sovelluksen kansioon.

## Perusversion tarjoama toiminnallisuus

### Tuotteen hakeminen

Käyttäjä voi hakea tuotetta tietokannasta kirjoittamalla tuotekenttään tuotteen nimen tai osan siitä, ja painamalla joko Enter-näppäintä tai "Etsi"-painiketta. Jos täysin samanniminen tuote löytyy tietokannasta ja vain yhdeltä osastolta, sovellus ilmoittaa käyttäjälle, että tuote löytyi ja valitsee oikean osaston tuotteelle.

Jos tietokannasta löytyy tuotteita, joiden nimi osin täsmää syötettyyn tuotenimeen tai tuote löytyy useammalta eri osastolta, sovellus ehdottaa käyttäjälle näitä tuotteita. Jos käyttäjä painaa tuote-ehdotuksia, sovellus täyttää kyseisen tuotteen koko nimen ja osaston syötekenttiin käyttäjän puolesta.

Jos mitään vastaavaa tuotetta ei löydy tietokannasta, sovellus ilmoittaa käyttäjälle ettei tuotetta löytynyt. 

### Tuotteen lisääminen kauppalistalle

Kun käyttäjä on täyttänyt kirjoituskenttään haluamansa tuotteen nimen ja määrän, sekä valinnut pudotusvalikosta määräyksikön, voi hän lisätä tuotteen kauppalistalle Enter+Control-näppäimillä tai "Lisää"-painikkeella.

Mikäli tuote on jo kauppalistalla, tuotteen lisääminen kasvattaa tuotteen valitun yksikön määrää.

Kun käyttäjä lisää tuotteen kauppalistalle, jos tuotetta ei jo löydy sovelluksen tuotetietokannasta, tallentaa sovellus tuotteen tietokantaan. 

### Tuotteiden hallinointi kauppalistalla

Kun tuotteita on lisätty kauppalistalle, voi käyttäjä poistaa tuotteita "x"-painikkeilla, jotka ovat kunkin tuotteen vieressä. Jos kaikki määrät tuotetta poistetaan, tuote poistuu kauppalistalta.

### Kauppalista tiedosto kokoaminen

Kun käyttäjä haluaa kauppalistan tiedostona ulos ohjelmasta, "laadi kauppalista"-painike kokoaa listan tuotteet tekstitiedostoon. Tiedostossa tuotteet ovat joateltu osastojen mukaan ja osastot järjetetty siihen järjetykseen kuin ne esiintyvät oletusruokakaupassa. "Laadi kauppalista"-painike avaa myös kyseisen tiedoston käyttöjärjestelmän oletussovelluksella tekstitiedostoille.

## Jatkokehitysideoita

Perusversion jälkeen sovellusta voidaan täydentää esim. seuraavilla toiminnallisuuksilla, mikäli aika sallii:

- Kauppalistan järjestely - käyttäjä voi valita minkä perusteella tuotteet järjestellään kauppalistaan ja/tai sovellusnäkymässä
- Osastojen järjestely mahdollisuus - käyttäjä voi järjestellä ruokakaupan osastot uuteen järjestykseen tai luoda kauppoja, joissa osastot ovat eri järjestyksessä
- Suosikkituotteiden valinta - käyttäjä voi valita suosikkituotteensa tuotetietokannasta
- Reseptien luonti - Käyttäjä voi luoda reseptejä, jolla käyttäjä saa lisättyä kaikki reseptin ainesosat kauppalistalle
- Käyttöliittymän jalostus - Käyttöliittymän ilme ja toiminnallisuudet tukevat parempaa käyttäjäkokemusta
