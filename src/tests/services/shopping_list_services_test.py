import unittest
from entities.product import Product
from entities.department import Department
from entities.store import Store
from services.shopping_list_services import Shopping_list_service


class FakeProductRepository:
    def __init__(self):
        self._products = [
            Product("omena", Department("hevi")),
            Product("maito", Department("maitotuotteet")),
            Product("ruisleipä", Department("leipä"))
        ]


class FakeStoreRepository:
    def __init__(self):
        self._stores = [Store("oletuskauppa", [
            Department("hevi"),
            Department("leipä"),
            Department("maito")])]

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]


class TestShoppingListService(unittest.TestCase):
    def setUp(self):
        self.shopping_list_service = Shopping_list_service(
            FakeProductRepository(), FakeStoreRepository())

        self.product_a = Product("ruisleipä", Department("leipä"))
        self.product_b = Product("päärynä", Department("hevi"))

    def test_get_department_order_in_store(self):
        department_order_in_store = self.shopping_list_service.get_department_order_in_store()

        self.assertEqual(len(department_order_in_store), 3)
        self.assertEqual(department_order_in_store[0].name, "hevi")
        self.assertEqual(department_order_in_store[1].name, "leipä")
        self.assertEqual(department_order_in_store[2].name, "maito")

    def test_get_current_shopping_list(self):
        current_shopping_list = self.shopping_list_service.get_current_shopping_list()

        self.assertEqual(len(current_shopping_list), 0)
