
import csv
from pathlib import Path

from entities.product import Product
from config import PRODUCT_REPOSITORY_PATH


class ProductRepository:
    def __init__(self):
        self._file_path = PRODUCT_REPOSITORY_PATH
        self._products = []
        self.pull_database()

    def get_products(self):
        return self._products

    def pull_database(self):
        self._ensure_file_exists()
        with open(self._file_path, mode='r', encoding='UTF-8') as product_file:
            for row in csv.reader(product_file, delimiter=';'):
                product_name = row[0]
                department = row[1]
                self._products.append(Product(product_name, department))

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def add_product(self, product_name: str, department: str):
        product = Product(product_name, department)
        self._products.append(product)
        with open(self._file_path, mode='a', encoding='UTF-8') as product_file:
            product_file.write(f'{product.name};{product.department}\n')
        return product

    def delete_all(self):
        self._products = []
        with open(self._file_path, mode='w', encoding='UTF-8'):
            pass
