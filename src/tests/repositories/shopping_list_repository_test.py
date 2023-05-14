
import unittest
from repositories.shopping_list_repository import ShoppingListRepository
from entities.product import Product


class TestShoppingListRepository(unittest.TestCase):
    def setUp(self):
        self.shopping_list_repository = ShoppingListRepository()

    def test_compile_shopping_list(self):
        department_order_in_store = ["hevi", "leipä", "maito"]
        product = Product("kiivi", "hevi")
        shopping_list = {}
        shopping_list[product] = {
            "kpl": 1,
            "ml": 0,
            "l": 0,
            "g": 0,
            "kg": 3,
        }
        self.shopping_list_repository.compile_shopping_list(
            department_order_in_store, shopping_list)
        with open(self.shopping_list_repository._file_path, mode="r", encoding="utf-8") as shopping_list_file:
            self.assertEqual(shopping_list_file.read(
            ), "Kauppalista\n\nHevi\n\n - Kiivi, 1 kpl + 3 kg\n\n")
