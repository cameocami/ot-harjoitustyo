from entities.department import Department
from entities.product import Product
from entities.store import Store
from repositories.product_repository import ProductRepository
from repositories.store_repository import StoreRepository


class Shopping_list_service:

    def __init__(self, product_repository: "ProductRepository", store_repository: "StoreRepository"):
        self._product_repository = product_repository
        self._current_shopping_list = {}
        self._store_repository = store_repository
        self._store = self._store_repository.get_store("oletuskauppa")

    def get_current_shopping_list(self):
        return self._current_shopping_list

    def get_department_order_in_store(self):
        return self._store.get_department_order_in_store()

    def find_product_department(self, product_name: str):
        for product in self._product_repository.get_products():
            if product.name == product_name.lower():
                return product.department
        return None

    def create_new_product(self, product_name: str, department: "Department"):
        product = Product(product_name, department)
        self._product_repository.add_product(product)
        return product

    def add_product_to_current_shopping_list(self, product: "Product", amount: int, unit: str):
        if product not in self._current_shopping_list.keys():
            self._current_shopping_list[product] = {
                "kpl": 0,
                "ml": 0,
                "l": 0,
                "g": 0,
                "kg": 0,
            }
        self._current_shopping_list[product][unit] += amount

    def compile_shopping_list(self):
        with open("kauppalista.txt", "w") as shopping_list_file:
            for department in self._store.get_department_order_in_store():
                shopping_list_file.write(f'{department}\n')
                for product, amounts in self._current_shopping_list.items():
                    if product.department == department:
                        row = product.name + amounts
                        shopping_list_file.write(row+"\n")

    def change_store(self, store_name):
        store = store_repository.get_store(store_name)
        self._store = store
