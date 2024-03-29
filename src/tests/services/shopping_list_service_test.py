import unittest
from entities.product import Product
from entities.store import Store
from services.shopping_list_services import ShoppingListService


class FakeProductRepository:
    def __init__(self):
        self._products = [
            Product("omena", "hevi"),
            Product("granaattiomena", "hevi"),
            Product("päärynä", "hevi"),
            Product("peruna", "hevi"),
            Product("sipuli", "hevi"),
            Product("maito", "maitotuotteet"),
            Product("omenarahka", "maitotuotteet"),
            Product("jogurtti", "maitotuotteet"),
            Product("kermaviili", "maitotuotteet"),
            Product("kuohukerma", "maitotuotteet"),
            Product("ruisleipä", "leipä"),
            Product("korvapuusti", "leipä"),
            Product("korvapuusti", "pakaste")
        ]

    def get_products(self):
        return self._products

    def add_product(self, product_name: str, department: str):
        product = Product(product_name, department)
        self._products.append(product)
        return product


class FakeStoreRepository:
    def __init__(self):
        self._stores = [Store("oletuskauppa", [
            "hevi",
            "leipä",
            "maito"]), Store("Alepa Kamppi", ["hevi", "valmisruoka", "makeiset"])]

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]


class FakeShoppingListRepository:
    def __init__(self):
        pass


class TestShoppingListService(unittest.TestCase):
    def setUp(self):
        self.shopping_list_service = ShoppingListService(
            FakeProductRepository(), FakeStoreRepository(), FakeShoppingListRepository())

    def test_get_current_shopping_list(self):
        current_shopping_list = self.shopping_list_service.get_current_shopping_list()

        self.assertEqual(len(current_shopping_list), 0)

    def test_get_department_order_in_store(self):
        department_order_in_store = self.shopping_list_service.get_department_order_in_store()

        self.assertEqual(len(department_order_in_store), 3)
        self.assertEqual(department_order_in_store[0], "hevi")
        self.assertEqual(department_order_in_store[1], "leipä")
        self.assertEqual(department_order_in_store[2], "maito")

    def test_find_product_with_exact_spelling_no_department(self):
        product_suggestion = self.shopping_list_service.find_product("omena")

        self.assertEqual(len(product_suggestion), 1)
        self.assertEqual(product_suggestion[0].name, "omena")
        self.assertEqual(product_suggestion[0].department, "hevi")

    def test_find_product_with_exact_spelling_correct_department(self):
        product_suggestion = self.shopping_list_service.find_product("korvapuusti", "pakaste")

        self.assertEqual(len(product_suggestion), 1)
        self.assertEqual(product_suggestion[0].name, "korvapuusti")
        self.assertEqual(product_suggestion[0].department, "pakaste")

    def test_find_product_with_exact_spelling_several_departments(self):
        product_suggestion = self.shopping_list_service.find_product("korvapuusti")

        self.assertEqual(len(product_suggestion), 2)
        self.assertEqual(product_suggestion[0].name, "korvapuusti")
        self.assertEqual(product_suggestion[0].department, "leipä")
        self.assertEqual(product_suggestion[1].name, "korvapuusti")
        self.assertEqual(product_suggestion[1].department, "pakaste")

    def test_form_suggestions_with_exact_spelling(self):
        product_suggestion = self.shopping_list_service.form_product_suggestions("omena")

        self.assertEqual(len(product_suggestion), 4)
        self.assertEqual(product_suggestion[0].name, "omena")
        self.assertEqual(product_suggestion[0].department, "hevi")


    def test_form_suggestions_with_partial_entry(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("mena")

        self.assertEqual(len(product_suggestions), 3)
        self.assertEqual(product_suggestions[0].name, "omena")
        self.assertEqual(product_suggestions[1].name, "granaattiomena")
        self.assertEqual(product_suggestions[2].name, "omenarahka")

    def test_form_suggestions_with_overextended_entry(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions(
            "granny smith omena")

        self.assertEqual(len(product_suggestions), 1)
        self.assertEqual(product_suggestions[0].name, "omena")

    def test_form_suggestions_with_one_double_character(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("omenna")

        self.assertEqual(len(product_suggestions), 1)
        self.assertEqual(product_suggestions[0].name, "omena")

    def test_form_suggestions_with_one_random_character_too_many(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("omebna")

        self.assertEqual(len(product_suggestions), 1)
        self.assertEqual(product_suggestions[0].name, "omena")

    def test_form_suggestions_with_one_character_missing(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("omna")

        self.assertEqual(len(product_suggestions), 1)
        self.assertEqual(product_suggestions[0].name, "omena")

    def test_form_suggestions_with_one_character_misspelt(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("omina")

        self.assertEqual(len(product_suggestions), 1)
        self.assertEqual(product_suggestions[0].name, "omena")
        self.assertEqual(product_suggestions[0].department, "hevi")

    def test_form_suggestions_with_too_many_suggestions(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions("")

        self.assertEqual(len(product_suggestions), 10)

    def test_form_suggestions_when_no_suggestions(self):
        product_suggestions = self.shopping_list_service.form_product_suggestions(
            "selleri")

        self.assertEqual(product_suggestions, [])

    def test_create_new_product(self):
        product = self.shopping_list_service.create_new_product(
            "paahtoleipä", "leipä")

        self.assertEqual(self.shopping_list_service._product_repository.get_products(
        )[-1].name, "paahtoleipä")
        self.assertEqual(self.shopping_list_service._product_repository.get_products(
        )[-1].department, "leipä")
        self.assertEqual(product.name, "paahtoleipä")
        self.assertEqual(product.department, "leipä")

    def test_add_new_product_to_current_shopping_list(self):
        product = Product("ruokakerma", "maito")
        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 200, "ml")

        self.assertEqual(
            list(self.shopping_list_service.get_current_shopping_list().keys()), [product])
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["kpl"], 0)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["ml"], 200)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["l"], 0)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["g"], 0)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["kg"], 0)

    def test_add_to_existing_product_to_current_shopping_list(self):
        product = Product("ruokakerma", "maito")
        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 200, "ml")
        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 1, "kpl")

        self.assertEqual(
            list(self.shopping_list_service.get_current_shopping_list().keys()), [product])
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["kpl"], 1)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["ml"], 200)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["l"], 0)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["g"], 0)
        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[
                         product]["kg"], 0)

    def test_delete_product_from_shopping_list(self):
        product = Product("makaronilaatikko", "valmisruoka")

        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 400, "g")
        self.shopping_list_service.delete_product_from_shopping_list(
            product, "g")

        self.assertEqual(
            self.shopping_list_service.get_current_shopping_list(), {})

    def test_reduce_amount_of_product_in_shopping_list(self):
        product = Product("makaronilaatikko", "valmisruoka")

        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 400, "g")
        self.shopping_list_service.add_product_to_current_shopping_list(
            product, 1, "kpl")
        self.shopping_list_service.delete_product_from_shopping_list(
            product, "g")

        self.assertEqual(self.shopping_list_service.get_current_shopping_list()[product], {
            "kpl": 1,
            "ml": 0,
            "l": 0,
            "g": 0,
            "kg": 0,
        })

    def test_empty_shopping_list(self):
        product = Product("makaronilaatikko", "valmisruoka")
        self.shopping_list_service.add_product_to_current_shopping_list(product, 1, "kpl")

        self.shopping_list_service.empty_shopping_list()

        self.assertEqual(self.shopping_list_service.get_current_shopping_list(), {})