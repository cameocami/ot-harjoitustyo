# Käyttöohje

Lataa projektin viimeisimmän [releasen]() lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

### Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi konfiguroida käynnistyshakemistossa _.env_-tiedostossa. Kun ohjelma käynnistetään tiedostot luodaan automaattisesti _data_-hakemistoon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```
PRODUCT_REPOSITORY = products.cvs
STORE_REPOSITORY = stores.cvs
SHOPPING_LIST = kauppalista.txt
```

### Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Ja käynnistä ohjelma komennolla:

```
poetry run invoke start
```
### Tuotten hakeminen

### Ehdotetun tuotteen valitseminen

### Tuotteen lisääminen listalle

### Tuoteen poistaminen listalta

### Kauppalistan tyhjetäminen

### Kauppalista-tiedoston laatiminen









