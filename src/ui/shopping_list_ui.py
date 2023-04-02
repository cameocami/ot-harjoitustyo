from tkinter import Tk, ttk, constants, StringVar

from services.shopping_list_services import shopping_list_service


class Main_View:
    def __init__(self, root):
        self._root = root
        self._options_menu = ttk.Frame(master=self._root)
        self._current_shopping_list = ttk.Frame(master=self._root)
        self._enter_items_menu = ttk.Frame(master=self._root)


    def display(self):
        self._form_options_menu()
        self._options_menu.pack()

        self._form_current_shopping_list()
        self._current_shopping_list.pack()

        self._form_enter_items_menu()
        self._enter_items_menu.pack()


    # Options menu

    def _form_options_menu(self):
        compile_shopping_list_button = ttk.Button(master=self._options_menu, text="Laadi kauppalista", command=shopping_list_service.compile_shopping_list())
        compile_shopping_list_button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)

    # Current shopping list

    def _form_current_shopping_list(self):
        for product, amounts in shopping_list_service.get_current_shopping_list():
            product_frame = ttk.Frame(master=self._current_shopping_list)
            product_label = ttk.Label(master=product_frame, text=product.name)
            product_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
            rows = 0
            for unit, amount in amounts.items():
                if amount > 0:
                    amount_label = ttk.Label(master=product_frame, text=f'{amount} {unit}')
                    amount_label.grid(row=rows, column=1, padx=5, pady=5, sticky=constants.W)
                    rows += 1
            product_frame.pack()

    # Enter products menu
    
    def _form_enter_items_menu(self):
        entry_frame = ttk.Frame(master=self._enter_items_menu)

        text = StringVar()
        product_entry = ttk.Entry(master=entry_frame, textvariable=text)
        product_entry.grid(row=0, column=0)

        amount = StringVar()
        amount_entry = ttk.Entry(master=entry_frame, textvariable=amount)
        amount_entry.grid(row=0, column=1)

        unit_options = ["kpl", "kpl", "ml", "l", "g","kg"]
        unit = StringVar()
        unit_option = ttk.OptionMenu(entry_frame, unit, *unit_options)
        unit_option.grid(row=0, column=2)

        entry_frame.pack()

            
"""
class Enter_items_frame:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)

        self._entry = ttk.Entry(master=self._frame)
        self._entry.pack()

        button = ttk.Button(
          master=self._frame,
          text="Lisää",
          command=self._handle_button_click
        )

        button.pack()

    def _handle_button_click(self):
        entry_value = self._entry.get()
        print(f"Tuote on: {entry_value}")
            
    def pack(self):
        self._frame.pack()
"""