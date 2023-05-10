from config import SHOPPING_LIST_PATH


class ShoppingListRepository:
    def __init__(self):
        self._file_path = SHOPPING_LIST_PATH

    def compile_shopping_list(self, shopping_list: dict()):
        with open(self._file_path, mode="w", encoding="utf-8") as shopping_list_file:
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
