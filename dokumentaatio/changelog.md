# Changelog

## Viikko 3

- Käyttäjä näkee käyttöliittymän, jossa on mahdolliset valinnat osastoista ja kirjoituskenttä tuotteiden nimiä varten
- Lisätty ShoppingListService-luokka, joka vastaa sovelluslogiikan koodista
- Lisätty ProductRepository-luokka, joka vastaa tuotteiden tallennuksesta CSV-tiedostoon
- Lisätty StoreRepository-luokka, joka vastaa osastojen järjestyksen tallenuksesta CSV-tiedostoon

## Viikko 4

- Käyttäjä voi etsiä tuotteen osaston tuotteen nimen perusteella
- Käyttäjä voi lisätä tuotteita sekä tietokantaan että kauppalistalle
- Käyttäjä näkee kauppalistalle lisätyt tuotteet
- Käyttäjä voi päivittää kauppalista-tekstitiedoston kauppalistan tuotteilla, osastojärjestyksessä
- Testattu, että ShoppingListService-luokka löytää tuotteet tietokannasta, osaa luoda uuden tuotteen, osaa lisätä tuotteita tämän hetkiselle kauppalistalle ja osaa vaihtaa kauppaa. 

## Viikko 5

- Kun käyttäjä etsii tuottetta nimen perusteella, eikä täysin saman nimistä tuotetta löydy, sovellus ehdottaa käyttäjälle:
  -  Tuotteita, joiden nimessä on yksi kirjain enemmän kuin hakusanassa
  -  Tuotteita, joiden nimessä on yksi kirjain vähemmän kuin hakusanassa
  -  Tuotteita, joiden nimessä on yksi kirjain on eri kuin hakusanassa
  -  Tuotteita, joiden nimessä hakusana esiintyy
  -  Tuotteita, joiden nimi esiintyy hakusanassa

## Viikko 6

## Viikko 7

- Käyttäjä voi poistaa kauppalistalta tuotteita poista-painikkeella
- Käyttäjä saa virheilmoituksen, jos tuote on kirjoitettu tai valittu väärin



