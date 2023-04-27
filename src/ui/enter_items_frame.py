from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton
from services.shopping_list_services import ShoppingListService
from entities.product import Product


class EnterItemsFrame:
    """Class responsible for Tkinter-frame with options for searching for products and adding them to shopping list
    
    Attributes:
        shopping_list_service: service class that controls the application logic
        frame: the master frame of the Tkinter-window into which the user interface is initialized
        product_suggestions: list of product suggestions for last entry
        display_shopping_list_changes: MainView method to display the changes in a different frame (the shopping list frame)

        entry_frame: subframe for elements related to typing the product name, entering the amounts and searching for department of the product
        entry_text: Tkinter-stringvariable for entered product name
        entry_amount: Tkinter stringvariable for entered amount
        option_unit: Tkinter stringvariable for chosen unit type

        departments_frame: subframe for elements for displaying all departments available and chosing the desired department
        radiobutton_department: Tkinter-integervariable for chosen department

        add_button_frame: subframe for elements for adding product to shopping list and product repository

    """
    def __init__(self, root, shopping_list_service: ShoppingListService, display_shopping_list_changes):
        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)
        self._product_suggestions = []
        self._display_shopping_list_changes = display_shopping_list_changes

    def pack(self):
        self._pack_entry_frame()
        self._pack_departments_frame()
        self._pack_add_product_button_frame()
        self._pack_suggestions_frame()
        self._frame.pack()

    def _pack_entry_frame(self):
        self._entry_frame = ttk.Frame(master=self._frame)

        self._entry_text = StringVar()
        product_entry = ttk.Entry(master=self._entry_frame, textvariable=self._entry_text)
        product_entry.grid(row=0, column=0)
        # self._product_entry.insert(0, "Lisää tuote kauppalistalle")

        self._entry_amount = StringVar()
        amount_entry = ttk.Entry(master=self._entry_frame, textvariable=self._entry_amount)
        amount_entry.grid(row=0, column=1)
        self._entry_amount.set(0)

        self._option_unit = StringVar()
        unit_options = ["kpl", "ml", "l", "g", "kg"]
        unit_option = ttk.OptionMenu(self._entry_frame, self._option_unit, unit_options[0], *unit_options)
        unit_option.grid(row=0, column=2)

        search_product_button = ttk.Button(master=self._entry_frame, text="Etsi", command=self._search_product_button_handler)
        search_product_button.grid(row=0, column=3)

        self._entry_frame.pack()

    def _pack_departments_frame(self):
        self._departments_frame = ttk.Frame(master=self._frame)

        self._radiobutton_department = IntVar()
        self._radiobutton_department.set(None)
        departments = sorted(self._shopping_list_service.get_department_order_in_store(), key=lambda x: str(x))
        position = 0
        grid_row = 0
        grid_column = 0
        for department in departments:
            department_selection = Radiobutton(
                master=self._departments_frame, text=department, indicatoron=0, variable=self._radiobutton_department, value=position)
            department_selection.grid(row=grid_row, column=grid_column)
            position += 1
            grid_row += 1
            if grid_row % 7 == 0:
                grid_row -= 7
                grid_column += 1

        self._departments_frame.pack()

    def _pack_add_product_button_frame(self):
        self._add_button_frame = ttk.Frame(master=self._frame)

        self._add_product_button = ttk.Button(
            self._add_button_frame, text="Lisää", command=self._add_product_button_handler)
        self._add_product_button.grid(sticky=constants.E)

        self._add_button_frame.pack()

    def _pack_suggestions_frame(self):

        self._suggestions_frame = ttk.Frame(master=self._frame)

        for product in self._product_suggestions:
            product_label = ttk.Label(
                master=self._suggestions_frame, text=product)
            product_label.pack()

        self._suggestions_frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _search_product_button_handler(self):
        product_entry = self._entry_text.get()
        self._product_suggestions = []
        if not self._check_product_entry_validity(product_entry):
            raise ValueError("Product name input incorrect")
        product_suggestion = self._shopping_list_service.find_product(
            product_entry)
        if product_suggestion[0]:
            product = product_suggestion[1]
            radiobutton_pos = self._find_selection_from_department(
                product.department)
            self._radiobutton_department.set(radiobutton_pos)
            self._product_suggestions.append("Tuote löytyi!")
        else:
            self._product_suggestions = product_suggestion[1]
            self._product_suggestions.insert(
                0, "Tuotetta ei löytynyt. Tarkoititko jotain seuraavista?")
            self._radiobutton_department.set(None)

        self._suggestions_frame.destroy()
        self._pack_suggestions_frame()

    def _add_product_button_handler(self):
        product_entry = self._entry_text.get()
        amount_entry = self._entry_amount.get()
        unit_option = self._option_unit.get()
        department_selection = self._radiobutton_department.get()

        if not self._check_product_entry_validity(product_entry):
            raise ValueError("Product name input incorrect")
        if not self._check_amount_entry_validity(amount_entry):
            raise ValueError("Amount input incorrect")
        if not self._check_department_selection_validity(department_selection):
            raise ValueError("Department not chosen")

        amount_entry = int(amount_entry)
        product_suggestion = self._shopping_list_service.find_product(
            product_entry)
        if product_suggestion[0]:
            product = product_suggestion[1]
        else:
            department = self._find_department_from_selection(
                department_selection)
            product = self._shopping_list_service.create_new_product(
                product_entry, department)
        self._shopping_list_service.add_product_to_current_shopping_list(
            product, amount_entry, unit_option)

        self._display_shopping_list_changes()
        self._entry_text.set("")
        self._entry_amount.set("")
        self._option_unit.set("kpl")
        self._radiobutton_department.set(None)
        self._product_suggestions = []
        self._suggestions_frame.destroy()

    def _check_product_entry_validity(self, product_entry):
        return True

    def _check_amount_entry_validity(self, amount_entry):
        return True

    def _check_department_selection_validity(self, department_selection):
        return True

    def _find_department_from_selection(self, department_selection):
        departments = sorted(self._shopping_list_service.get_department_order_in_store(), key=lambda x: str(x))
        return departments[department_selection]

    def _find_selection_from_department(self, department_name):
        departments = sorted(self._shopping_list_service.get_department_order_in_store(), key=lambda x: str(x))
        for department in departments:
            if department.name.lower() == department_name.lower():
                return departments.index(department)
