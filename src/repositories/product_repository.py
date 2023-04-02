
import csv
from entities.product import Product


class ProductRepository:
    def __init__(self):
        self._products = []
    
    def pull_database(self):
        with open("products.cvs") as product_file:
            for row in csv.reader(product_file, delimiter=";"):
                self._products.append(Product(row[0], row[1]))
    
    def save_to_database(self):
        with open("products.cvs", 'w') as product_file:
            for product in self._products:
                product_file.write(f'{product.name};{product.department}\n')

    def add_to_database(self, product: "Product"):
        with open("products.cvs", 'a') as product_file:
            product_file.write(f'{product.name};{product.department}\n')

    