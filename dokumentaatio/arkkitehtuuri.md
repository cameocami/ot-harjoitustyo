# Arkkitehtuurikuvaus

### Rakenne

Ohjelman rakenne on neljässä tasossa. Koodin pakkausrakenne on seuraava:

<img src="https://github.com/cameocami/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/pakkauskaavio.png" alt="Pakkauskaavio" width="25%" height="25%" />

Pakkaus nimeltä UI vastaa käyttöliittymän koodista. Services-pakkaus vastaa sovelluslogiikasta. Repositories-pakkaus vastaa pysyväistallennukseen liittyvästä koodista ja Entities-pakkaus vastaa sovelluksessa käytössä olevista oliosta. 

### Käyttöliittymä

Käyttöliittymässä on yksi näkymä, joka on jaoteltu kolmeen osioon: 

- Valinnat 
- Kauppalista 
- Tuotteiden lisäys

Kukin näistä on toteutettu omana luokkanaan. UI-luokka vastaa osioiden pakkaamisesta järjestyksessä. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Käyttöliittymä kutsuu ShoppingListService-luokan metodeja.

### Sovelluslogiikka

Luokat Product ja Store muodostavat sovelluksen perusyksiköt. Product-olio kuvaa tuotteen tietoja:

```mermaid
 classDiagram
      class Product{
          name
          department
      }
```
Store-olio kuvaa kaupan tietoja:

```mermaid
 classDiagram
      class Store{
          name
          departments
      }
```
Sovelluksen toiminnallisesta kokonaisuudesta vastaa ShoppingListService-luokka. ShoppingListService-olio tarjoaa käyttöliittymälle metodit, joita se tarvitsee kullekkin toiminnolle. Esimerkkejä ovat:

- get_current_shopping_list()
- find_product(product_entry, department)    
- create_new_product(product_name, department)
- add_product_to_current_shopping_list(product, amount, unit)
- delete_product_from_shopping_list(product, unit)

Repositories-pakkauksessa sijatsevat ProductRepository, ShoppingListRepository ja StoreRepository tarjoavat ShoppingListService-oliolle pääsyn Product- ja Store-olioihin. ProductRepository ja StoreRepository-luokat tarjovat ShoppingListService-oliolle pysyväistallennuksen perusyksiköiden tiedoista. ShoppingListRepository-luokka tarjoaa käyttäjälle kauppalista-tiedoston pysyväistallennuksen. Luokkien toteutukset injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

Ohessa pakkauskaavio, joka kuvaa ShoppingListService-luokan suhdetta ohjelman muihin osiin:



### Tietojen pysyväistallennus

Repositories-pakkauksessa sijatsevat ProductRepository ja StoreRepository ovat vastuussa tietojen pysyväistallennuksesta. Nämä tallentavat tiedot CSV-tiedostoihin. ShoppingListRepository vastaa "Kauppalista"-tekstitiedoston luonnista ja tallennuksesta. 

Luokat pyrkivät noudattamaan Repository -suunnittelumallia.  Luokat voidaan tarvittaessa korvata uusilla toteutuksilla, esimerkiksi SQL-tietokannoilla. Sovelluslogiikan testauksessa käytetään tiedostoon ja tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

#### Tiedostot

Sovellus tallettaa tuotteiden ja kauppojen tiedot erillisiin tiedostoihin. 

Sovelluksen juureen sijoitettu konfiguraatiotiedosto [.env](././.env) määrittelee tiedostojen nimet.

Sovellus tallettaa tehtävät CSV-tiedostoon seuraavassa formaatissa:

```
vehnäjauho;kuivatuotteet
vaniljajäätelö;pakasteet
```
Eli ensimmäiseksi tuotteen nimi ja sitten tuotteen osasto. Kenttien arvot erotellaan puolipisteellä (;).

### Päätoiminnallisuudet

Seauraava sekvenssikaavio kuvaa sovelluksen toimintalogiikkaa erään päätoiminnallisuuden osalta:

#### Tuotteen lisääminen kauppalistalle

Kun tuotekentään kirjoitetaan tuote ja tämän jälkeen klikataan _Lisää_, etenee sovellus seurvaasti:

```mermaid
sequenceDiagram

  actor User
  participant Ui
  participant EnterItemsFrame
  participant ShoppingListService
  participant ProductRepository

  User ->> EnterItemsFrame: click "Lisää" button
  
  EnterItemsFrame -> EnterItemsFrame: _check_product_entry_validity()
  EnterItemsFrame -> EnterItemsFrame: _check_amount_entry_validity()
  EnterItemsFrame -> EnterItemsFrame: _check_department_selection_validity()
  EnterItemsFrame -> EnterItemsFrame: _find_department_from_selection(1: radiobutton value)

  EnterItemsFrame ->> ShoppingListService: find_product("omena", "hedelmät ja vihannekset")
  ShoppingListService ->> ProductRepository: get_products()
  ProductRepository -->> ShoppingListService: list
  ShoppingListService -->> EnterItemsFrame: (True, product)
  EnterItemsFrame ->> ShoppingListService: add_product_to_current_shopping_list(product, 3, "kpl")
  EnterItemsFrame -> Ui: display_shopping_list_changes()
  
  Ui -> ShoppingListFrame: pack()
  ShoppingListFrame ->> ShoppingListService: get_current_shopping_list()
  ShoppingListService -->> EnterItemsFrame: dict  
  
```
Painikkeseen reagoiva tapahtumankäsittelijä ensin tarkistaa syötteiden oikeellisuuden kutsumalla sen omia metodeja check_product_entry_validity, check_amount_entry_validity ja check_department_selection_validity. Kun syötteet ovat oikein, käyttöliittymän luokka EnterItemsFrame kutsuu sen omaa metodia find_department_from_selection valintapainikkeen arvolla. Tämän jälkeen EnterItemsFrame kutsuu sovelluslogiikan ShoppingListService metodia find_product tuotekenttään syötyllä arvolla ja valitulla osastolla. Sovelluslogiikka kutsuu ProductRepository tietokannan metodia get_products(), joka palauttaa listan tietokannassa olevista tuotteista. Sovelluslogiikka ShoppingListService etsii syötettyjen arvojen perusteella oikean tuotteen tuotelistasta. Ja palauttaa käyttöliittymän luokalle EnterItemsFrame tuplen, jonka ensimmäinen arvo on True, koska tuote löytyi tietokannasta, ja toinen arvo on itse tuote. Tämän jälkeen EnterItemsFrame kutsuu ShoppingListServicen metodia add_product_to_current_shopping_list parametreinään tuote, määrä ja yksikkö. 

### Ohjelman rakenteeseen jääneet heikkoudet
