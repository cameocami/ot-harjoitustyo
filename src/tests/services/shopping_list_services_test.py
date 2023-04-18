import unittest
from entities.product import Product
from entities.department import Department
from entities.store import Store
from services.shopping_list_services import ShoppingListService


class FakeProductRepository:
    def __init__(self):
        self._products = [
            Product("omena", Department("hevi")),
            Product("maito", Department("maitotuotteet")),
            Product("ruisleipä", Department("leipä"))
        ]

    def get_products(self):
        return self._products

    def add_product(self, product_name: str, department: "Department"):
        product = Product(product_name, department)
        self._products.append(product)
        return product


class FakeStoreRepository:
    def __init__(self):
        self._stores = [Store("oletuskauppa", [
            Department("hevi"),
            Department("leipä"),
            Department("maito")]), Store("Alepa Kamppi", [Department("hevi"), Department("valmisruoka"), Department("makeiset")])]

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]


class TestShoppingListService(unittest.TestCase):
    def setUp(self):
        self.shopping_list_service = ShoppingListService(
            FakeProductRepository(), FakeStoreRepository())

        self.product_a = Product("ruisleipä", Department("leipä"))
        self.product_b = Product("päärynä", Department("hevi"))

    def test_get_current_shopping_list(self):
        current_shopping_list = self.shopping_list_service.get_current_shopping_list()

        self.assertEqual(len(current_shopping_list), 0)

    def test_get_department_order_in_store(self):
        department_order_in_store = self.shopping_list_service.get_department_order_in_store()

        self.assertEqual(len(department_order_in_store), 3)
        self.assertEqual(department_order_in_store[0].name, "hevi")
        self.assertEqual(department_order_in_store[1].name, "leipä")
        self.assertEqual(department_order_in_store[2].name, "maito")

    def test_find_product(self):
        found_product = self.shopping_list_service.find_product("omena")

        self.assertEqual(found_product.department.name, "hevi")

    def test_find_product_when_not_in_product_repo(self):
        found_product = self.shopping_list_service.find_product("selleri")

        self.assertEqual(found_product, None)

    def test_create_new_product(self):
        product = self.shopping_list_service.create_new_product(
            "paahtoleipä", Department("leipä"))

        self.assertEqual(self.shopping_list_service._product_repository.get_products(
        )[-1].name, "paahtoleipä")
        self.assertEqual(self.shopping_list_service._product_repository.get_products(
        )[-1].department.name, "leipä")
        self.assertEqual(product.name, "paahtoleipä")
        self.assertEqual(product.department.name, "leipä")

    def test_add_new_product_to_current_shopping_list(self):
        product = Product("ruokakerma", Department("maito"))
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
        product = Product("ruokakerma", Department("maito"))
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

    def test_change_store(self):
        self.shopping_list_service.change_store("Alepa Kamppi")

        self.assertEqual(
            self.shopping_list_service._store.name, "Alepa Kamppi")
