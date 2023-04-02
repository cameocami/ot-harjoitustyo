from entities.product import Product
from entities.department import Department
from repositories.product_repository import ProductRepository

class Shopping_list_service:

    def __init__(self):
        self._product_repository = ProductRepository()
        self._current_shopping_list = {}       

    def get_current_shopping_list(self):
        return self._current_shopping_list
    
    def find_product_department(self, product_name: str, amount: int, unit: str):
        for product in self._product_repository:
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

    
shopping_list_service = Shopping_list_service()