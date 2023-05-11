
import unittest

from repositories.store_repository import StoreRepository
from entities.store import Store


class TestStoreRepository(unittest.TestCase):
    def setUp(self):
        self.store_repository = StoreRepository()
        self.store_repository.delete_all()

    def test_get_empty_store_repository(self):
        stores = self.store_repository.get_store_repository()

        self.assertEqual((len(stores)), 0)

    def test_get_store_repository(self):
        name = "Alepa Kamppi"
        departments = ["hevi", "valmisruoka", "makeiset"]
        self.store_repository._stores = [Store(name, departments)]

        stores = self.store_repository.get_store_repository()

        self.assertEqual((len(stores)), 1)
        self.assertEqual(stores[0].name, "Alepa Kamppi")
        self.assertEqual(stores[0].departments[0], "hevi")
        self.assertEqual(stores[0].departments[1], "valmisruoka")
        self.assertEqual(stores[0].departments[2], "makeiset")


    def test_get_store_by_name(self):
        store1 = Store("Oletuskauppa", ["hevi", "valmisruoka", "makeiset"])
        store2 = Store("K-market Kamppi", ["hevi", "leipä", "maito"])
        self.store_repository._stores = [store1, store2]

        found_store = self.store_repository.get_store("K-market Kamppi")

        self.assertEqual(found_store.name, "K-market Kamppi")
        self.assertEqual(found_store.departments, ["hevi", "leipä", "maito"])

    def test_get_store_not_found(self):
        store1 = Store("Oletuskauppa", ["hevi", "valmisruoka", "makeiset"])
        store2 = Store("K-market Kamppi", ["hevi", "leipä", "maito"])
        self.store_repository._stores = [store1, store2]

        found_store = self.store_repository.get_store("K-supermarket Kamppi")

        self.assertEqual(found_store.name, "Oletuskauppa")
        self.assertEqual(found_store.departments, ["hevi", "valmisruoka", "makeiset"])

        