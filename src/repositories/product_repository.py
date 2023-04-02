
import csv
from entities.product import Product
from entities.department import Department

class ProductRepository:
    def __init__(self):
        self._products = []

    def get_product_repository(self):
        return self._products 
    
    def pull_database(self):
        with open("products.cvs") as product_file:
            for row in csv.reader(product_file, delimiter=";"):
                name = row[0]
                department = row[1]
                self._products.append(Product(name, department))
    
    def save_to_database(self):
        with open("products.cvs", 'w') as product_file:
            for product in self._products:
                product_file.write(f'{product.name};{product.department}\n')

    def add_product(self, product: "Product"):
        self._products.append(product)
        with open("products.cvs", 'a') as product_file:
            product_file.write(f'{product.name};{product.department}\n')
    