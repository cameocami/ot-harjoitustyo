from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton

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
        product_inputs = self._form_entry_bar()
        department_input = self._form_departments_tab()


    def _form_entry_bar(self):
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

        return [text, amount, unit]

    def _form_departments_tab(self):
        departments_frame = ttk.Frame(master=self._enter_items_menu)

        

        chosen_department = IntVar()
        chosen_department.set(0)
        position = 0
        grid_row = 0
        grid_column = 0

        departments = sorted(shopping_list_service.get_department_order_in_store(), key=lambda x: str(x))

        for department in departments:
            department_selection = Radiobutton(departments_frame, text=department,indicatoron=0, variable=chosen_department, value=position)
            department_selection.grid(row=grid_row, column = grid_column)
            position += 1
            grid_row += 1
            if grid_row % 7 == 0:
                grid_row -= 7
                grid_column += 1

        departments_frame.pack()

        return chosen_department.get()