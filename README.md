# Kauppalista app 

Sovelluksen avulla käyttäjä voi luoda kauppalistan haluamistaan ruokakaupan tuotteista. Valmis kauppalista, jossa tuotteet ovat osastoittain siinä järjestyksessä kun ne esiintyvät kaupssa tallentuu juurikansioon nimellä kauppalista.txt. Sovelluksessa käyttäjä voi käyttää tietokannan tuotteita, tai luoda uusia tuotteita kirjoittamalla niille nimen ja valitsemalla niille osaston.  

## Komentorivitoiminnot

### Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```
### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
## Dokumentaatio

- [Käyttöohje (tyhjä)](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti (tyhjä)](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
