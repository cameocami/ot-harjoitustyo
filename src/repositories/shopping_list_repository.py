from pathlib import Path
from startfile import startfile
from config import SHOPPING_LIST_PATH


class ShoppingListRepository:
    def __init__(self):
        self._file_path = SHOPPING_LIST_PATH

    def compile_shopping_list(self, department_order_in_store: list, shopping_list: dict):
        text = "Kauppalista\n\n"
        products_under_departments = self._sort_products(
            department_order_in_store, shopping_list)
        for department in products_under_departments:
            text += f'{department[0].capitalize()}\n\n'
            for product in department[1]:
                text += f' - {product[0]}, '
                text += self._amount_str_from_amount_dict(product[1])
                text += "\n"
            text += "\n"
        self._ensure_file_exists()
        with open(self._file_path, mode="w", encoding="utf-8") as shopping_list_file:
            shopping_list_file.write(text)

    def open_shopping_list_file(self):
        startfile(self._file_path)

    def _sort_products(self, department_order_in_store: list, shopping_list: dict):
        departments_with_list_of_products = []
        for department in department_order_in_store:
            products = []
            for product in shopping_list.keys():
                if product.department == department:
                    products.append((str(product), shopping_list[product]))
            products = sorted(products, key=lambda x: x[0])
            departments_with_list_of_products.append((department, products))
        return departments_with_list_of_products

    def _amount_str_from_amount_dict(self, amounts: dict):
        amount_str = ""
        several_units = False
        for unit, amount in amounts.items():
            if amount > 0:
                if several_units:
                    amount_str += ' + '
                amount_str += f'{amount} {unit}'
                several_units = True
        return amount_str

    def _ensure_file_exists(self):
        Path(self._file_path).touch()
