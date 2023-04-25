# Arkkitehtuurikuvaus

### Rakenne

Ohjelman rakenne on neljässä tasossa. Koodin pakkausrakenne on seuraava:

<img src="https://github.com/cameocami/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/pakkauskaavio.png" alt="Pakkauskaavio" width="25%" height="25%" />

Pakkaus nimeltä UI vastaa käyttöliittymän koodista. Services-pakkaus vastaa sovelluslogiikasta. Repositories-pakkaus vastaa pysyväistallennukseen liittyvästä koodista ja Entities-pakkaus vastaa sovelluksessa käytössä olevista oliosta. 

### Käyttöliittymä


### Sovelluslogiikka


### Tietojen pysyväistallennus


### Päätoiminnallisuudet

Seauraava sekvenssikaavio kuvaa sovelluksen toimintalogiikkaa erään päätoiminnallisuuden osalta:

#### Tuotteen lisääminen kauppalistalle

Kun tuotekentään kirjoitetaan tuote ja tämän jälkeen klikataan _Lisää_, etenee sovellus seurvaasti:

```mermaid
sequenceDiagram

  actor User
  participant Ui
  participant ShoppingListService
  participant ProductRepository

  User ->> Ui: click "Lisää" button
  Ui ->> ShoppingListService: find_product("omena")
  ShoppingListService ->> ProductRepository: get_products()
  ProductRepository -->> ShoppingListService: list
  ShoppingListService -->> Ui: (True, product)
  Ui ->> ShoppingListService: add_product_to_current_shopping_list(product, 3, "kpl")
  Ui -> Ui: display_shopping_list_changes()
  Ui ->> ShoppingListService: get_current_shopping_list()
  ShoppingListService -->> Ui: dict
  
```


### Ohjelman rakenteeseen jääneet heikkoudet
