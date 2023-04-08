from tkinter import ttk, constants
from services.shopping_list_services import ShoppingListService

class OptionsFrame:
    def __init__(self, root, shopping_list_service):
        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)
        self._compile_shopping_list_button = ttk.Button(
            master=self._frame, text="Laadi kauppalista", command=self._compile_shopping_list_button_handler)
        self._compile_shopping_list_button.grid(
            row=0, column=0, padx=5, pady=5, sticky=constants.E)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _compile_shopping_list_button_handler(self):
        self._shopping_list_service.compile_shopping_list()