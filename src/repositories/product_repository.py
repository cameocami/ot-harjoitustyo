
import csv
from entities.product import Product


class ProductRepository:
    def __init__(self):
        self._products = []
        self.pull_database()

    def get_products(self):
        return self._products

    def pull_database(self):
        with open('products.cvs', mode='r', encoding='UTF-8') as product_file:
            for row in csv.reader(product_file, delimiter=';'):
                name = row[0]
                department = row[1]
                self._products.append(Product(name, department))

    def save_to_database(self):
        with open('products.cvs', mode='w', encoding='UTF-8') as product_file:
            for product in self._products:
                product_file.write(f'{product.name};{product.department}\n')

    def add_product(self, product: 'Product'):
        self._products.append(product)
        with open('products.cvs', mode='a', encoding='UTF-8') as product_file:
            product_file.write(f'{product.name};{product.department}\n')
