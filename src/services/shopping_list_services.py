
from repositories.product_repository import ProductRepository
from repositories.store_repository import StoreRepository


class ShoppingListService:

    def __init__(self, product_repository: ProductRepository, store_repository: StoreRepository):
        self._product_repository = product_repository
        self._current_shopping_list = {}
        self._store_repository = store_repository
        self._store = self._store_repository.get_store("oletuskauppa")

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

    def create_new_product(self, product_name: str, department: "Department"):
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
        with open("kauppalista.txt", mode="w", encoding="utf-8") as shopping_list_file:
            for department in self._store.get_department_order_in_store():
                shopping_list_file.write(f'{department}\n')
                for product, amounts in self._current_shopping_list.items():
                    if product.department == department.name:
                        shopping_list_file.write(str(product) + ", ")
                        several_units = False
                        for unit, amount in amounts.items():
                            if amount > 0:
                                if several_units:
                                    shopping_list_file.write(' + ')
                                shopping_list_file.write(f'{amount} {unit}')
                                several_units = True
                        shopping_list_file.write("\n")
                shopping_list_file.write("\n")

    def change_store(self, store_name):
        store = self._store_repository.get_store(store_name)
        self._store = store
