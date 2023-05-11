
import unittest
from repositories.product_repository import ProductRepository


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        self.product_repository = ProductRepository()
        self.product_repository.delete_all()

    def test_get_products(self):
        products = self.product_repository.get_products()

        self.assertEqual((len(products)), 0)

    def test_add_product_return_value(self):
        product_name = "paahtoleipä"
        department = "leipä"
        product = self.product_repository.add_product(product_name, department)

        self.assertEqual(product.name, "paahtoleipä")
        self.assertEqual(product.department, "leipä")

    def test_add_product(self):
        product_name = "paahtoleipä"
        department = "leipä"
        self.product_repository.add_product(product_name, department)
        products = self.product_repository.get_products()

        self.assertEqual((len(products)), 1)
        self.assertEqual(products[0].name, "paahtoleipä")
        self.assertEqual(products[0].department, "leipä")
