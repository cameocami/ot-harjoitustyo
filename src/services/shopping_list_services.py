
from repositories.product_repository import ProductRepository
from repositories.store_repository import StoreRepository
from repositories.shopping_list_repository import ShoppingListRepository


class ShoppingListService:

    def __init__(self, product_repository: ProductRepository, store_repository: StoreRepository, shopping_list_repository: ShoppingListRepository):
        self._product_repository = product_repository
        self._current_shopping_list = {}
        self._store_repository = store_repository
        self._store = self._store_repository.get_store("oletuskauppa")
        self._shopping_list_repository = shopping_list_repository

    def get_current_shopping_list(self):
        return self._current_shopping_list

    def get_department_order_in_store(self):
        return self._store.get_department_order_in_store()

    def find_product(self, product_entry: str):
        suggestions = []
        product_entry = product_entry.lower()
        for product in self._product_repository.get_products():
            if product.name == product_entry:
                return (True, product)
            if product_entry in product.name:
                suggestions.append(product)
            elif product.name in product_entry:
                suggestions.append(product)
            elif len(product_entry) > len(product.name):
                for i in range(len(product_entry)):
                    suggestion = product_entry[:i] + product_entry[i+1:]
                    if product.name == suggestion:
                        suggestions.append(product)
                        break
            elif len(product_entry) < len(product.name):
                for i in range(len(product.name)):
                    product_misspelling = product.name[:i] + product.name[i+1:]
                    if product_misspelling == product_entry:
                        suggestions.append(product)
                        break
            elif len(product_entry) == len(product.name):
                for i in range(len(product.name)):
                    product_misspelling = product.name[:i] + product.name[i+1:]
                    suggestion = product_entry[:i] + product_entry[i+1:]
                    if product_misspelling == suggestion:
                        suggestions.append(product)
                        break
            if len(suggestions) > 9:
                break
        return (False, suggestions)

    def create_new_product(self, product_name: str, department: str):
        product = self._product_repository.add_product(
            product_name, department)
        return product

    def add_product_to_current_shopping_list(self, product: "Product", amount: int, unit: str):
        if product not in self._current_shopping_list:
            self._current_shopping_list[product] = {
                "kpl": 0,
                "ml": 0,
                "l": 0,
                "g": 0,
                "kg": 0,
            }
        self._current_shopping_list[product][unit] += amount

    def compile_shopping_list(self):
        self._shopping_list_repository.compile_shopping_list(
            self._store.get_department_order_in_store(), self._current_shopping_list)

    def delete_product_from_shopping_list(self, product, unit):
        self._current_shopping_list[product][unit] = 0

        all_amounts_at_zero = True
        amounts = self._current_shopping_list[product]
        for units in amounts:
            if amounts[units] > 0:
                all_amounts_at_zero = False
        if all_amounts_at_zero:
            self._current_shopping_list.pop(product)
