from tkinter import ttk, constants
from services.shopping_list_services import ShoppingListService

class ShoppingListFrame:
    def __init__(self, root, shopping_list_service: ShoppingListService):
        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)

    def pack(self):
        for product, amounts in self._shopping_list_service.get_current_shopping_list():
            product_frame = ttk.Frame(master=self._frame)
            product_label = ttk.Label(master=product_frame, text=product.name)
            product_label.grid(row=0, column=0, padx=5,
                               pady=5, sticky=constants.W)
            rows = 0
            for unit, amount in amounts.items():
                if amount > 0:
                    amount_label = ttk.Label(
                        master=product_frame, text=f'{amount} {unit}')
                    amount_label.grid(row=rows, column=1,
                                      padx=5, pady=5, sticky=constants.W)
                    rows += 1
            product_frame.pack()
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
