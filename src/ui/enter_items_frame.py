from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton
from services.shopping_list_services import ShoppingListService
from entities.product import Product


class EnterItemsFrame:
    """Class responsible for Tkinter-frame with options for searching for products and adding them to shopping list

    Attributes:
        shopping_list_service: service class that controls the application logic
        frame: the main frame for all elements in the enter items frame

        entry_frame: subframe for elements related to typing the product name, entering the amounts and searching for department of the product
        product_suggestions_frame: subframe for list of product suggestions
        departments_frame: subframe for displaying all departments available and chosing the desired department
        add_button_frame: subframe for the button for adding a product to shopping list and product repository
        error_messages_frame = subframe for list of errors

        entry_text: Tkinter-stringvariable for entered product name
        entry_amount: Tkinter stringvariable for entered amount
        option_unit: Tkinter stringvariable for chosen unit type
        radiobutton_department: Tkinter-integervariable for chosen department

        product_suggestions: list of suggestions for user when product not found when searched
        error_messages: list of error messages for invalid inputs

        display_shopping_list_changes: MainView method to display the changes in a different frame (the shopping list frame)
    """

    def __init__(self, root, shopping_list_service: ShoppingListService, display_shopping_list_changes):
        self._shopping_list_service = shopping_list_service

        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._entry_frame = None
        self._product_suggestions_frame = None
        self._departments_frame = None
        self._add_button_frame = None
        self._error_messages_frame = None

        self._entry_text = StringVar()
        # self._entry_text.set("Lisää tuote kauppalistalle")
        self._entry_amount = StringVar()
        self._entry_amount.set(0)
        self._option_unit = StringVar()
        self._radiobutton_department = IntVar()
        self._radiobutton_department.set(None)

        self._error_messages = []
        self._product_suggestions = []

        self._display_shopping_list_changes = display_shopping_list_changes

    def pack(self):

        self._form_entry_frame()
        self._form_product_suggestions_frame()
        self._form_departments_frame()
        self._form_add_product_button_frame()
        self._form_error_messages_frame()
        self._form_product_suggestions_frame()

        self._entry_frame.pack()
        self._product_suggestions_frame.pack()
        self._departments_frame.pack()
        self._add_button_frame.pack()
        self._error_messages_frame.pack()
        self._frame.pack()

    def _form_entry_frame(self):

        if self._entry_frame:
            self._entry_frame.destroy()

        self._entry_frame = ttk.Frame(master=self._frame)

        product_entry = ttk.Entry(
            master=self._entry_frame, width=46, textvariable=self._entry_text)
        product_entry.grid(row=0, column=0)

        amount_entry = ttk.Entry(
            master=self._entry_frame, width=10, textvariable=self._entry_amount)
        amount_entry.grid(row=0, column=1)

        unit_options = ["kpl", "ml", "l", "g", "kg"]
        unit_option = ttk.OptionMenu(
            self._entry_frame, self._option_unit, unit_options[0], *unit_options)
        unit_option.config(width=3)
        unit_option.grid(row=0, column=2)

        search_product_button = ttk.Button(
            master=self._entry_frame, width=9, text="Etsi", command=self._search_product_button_handler)
        search_product_button.grid(row=0, column=3)

    def _form_product_suggestions_frame(self):

        if self._product_suggestions_frame:
            self._product_suggestions_frame.destroy()

        self._product_suggestions_frame = ttk.Frame(master=self._frame)

        heading = True
        for product in self._product_suggestions:
            if heading:
                heading_label = ttk.Label(
                    master=self._product_suggestions_frame, text=product)
                heading_label.pack()
                heading = False
            else:
                product_suggestion_button = ttk.Button(
                    master=self._product_suggestions_frame, text=f'{product}, {product.department}', command=lambda arg1=product: self._product_suggestion_button_handler(arg1))
                product_suggestion_button.pack()

    def _product_suggestion_button_handler(self, product):
        self._set_chosen_product(product)

    def _set_chosen_product(self, product):
        radiobutton_pos = self._find_selection_from_department(
            product.department)
        self._radiobutton_department.set(radiobutton_pos)
        self._entry_text.set(product)

    def _form_departments_frame(self):

        if self._departments_frame:
            self._departments_frame.destroy()

        self._departments_frame = ttk.Frame(master=self._frame)

        departments = sorted(
            self._shopping_list_service.get_department_order_in_store())
        position = 0
        grid_row = 0
        grid_column = 0
        for department in departments:
            department_selection = Radiobutton(
                master=self._departments_frame, width=25, text=department.capitalize(), indicatoron=0, variable=self._radiobutton_department, value=position)
            department_selection.grid(row=grid_row, column=grid_column)
            position += 1
            grid_column += 1
            if grid_column % 3 == 0:
                grid_column -= 3
                grid_row += 1

    def _form_add_product_button_frame(self):

        if self._add_button_frame:
            self._add_button_frame.destroy()

        self._add_button_frame = ttk.Frame(master=self._frame)

        self._add_product_button = ttk.Button(
            self._add_button_frame, text="Lisää", command=self._add_product_button_handler)
        self._add_product_button.grid(sticky=constants.E)

    def _form_error_messages_frame(self):

        if self._error_messages_frame:
            self._error_messages_frame.destroy()

        self._error_messages_frame = ttk.Frame(master=self._frame)

        for error in self._error_messages:
            error_label = ttk.Label(
                master=self._error_messages_frame, text=error)
            error_label.pack()

    def _destroy(self):

        if self._entry_frame:
            self._entry_frame.destroy()

        if self._product_suggestions_frame:
            self._product_suggestions_frame.destroy()

        if self._departments_frame:
            self._departments_frame.destroy()

        if self._add_button_frame:
            self._add_button_frame.destroy()

        if self._error_messages_frame:
            self._error_messages_frame.destroy()

    def search_product_button_handler(self):
        self._product_suggestions = []
        self._error_messages = []

        if self._check_product_entry_validity():
            product_entry = self._entry_text.get().lower()
            found_products = self._shopping_list_service.find_product(
                product_entry)

            if len(found_products) == 1:
                product = found_products[0]
                self._set_chosen_product(product)
                self._product_suggestions = ["Tuote löytyi!"]

            elif len(found_products) > 1:
                self._product_suggestions = found_products
                heading = "Löytyi useampi tuote:"
                self._product_suggestions.insert(0, heading)
                self._radiobutton_department.set(None)

            else:
                self._product_suggestions = self._shopping_list_service.form_product_suggestions(
                    product_entry)
                heading = "Tuotetta ei löytynyt."
                if len(self._product_suggestions) == 1:
                    heading += " Tarkoititko?"
                elif len(self._product_suggestions) > 1:
                    heading += " Tarkoititko jotain seuraavista:"
                self._product_suggestions.insert(0, heading)
                self._radiobutton_department.set(None)

        self.pack()

    def add_product_button_handler(self):

        self._product_suggestions = []
        self._error_messages = []

        entry_valid = self._check_product_entry_validity()
        amount_valid = self._check_amount_entry_validity()
        department_valid = self._check_department_selection_validity()

        if entry_valid and amount_valid and department_valid:
            product_entry = self._entry_text.get().lower()
            amount_entry = int(self._entry_amount.get())
            unit_option = self._option_unit.get()
            selected_department = self._find_department_from_selection(
                self._radiobutton_department.get())

            found_products = self._shopping_list_service.find_product(
                product_entry, selected_department)

            if len(found_products) == 1:
                product = found_products[0]
            else:
                product = self._shopping_list_service.create_new_product(
                    product_entry, selected_department)

            self._shopping_list_service.add_product_to_current_shopping_list(
                product, amount_entry, unit_option)

            self._display_shopping_list_changes()
            self._entry_text.set("")
            self._entry_amount.set("")
            self._option_unit.set("kpl")
            self._radiobutton_department.set(None)
            self._product_suggestions = []
            self._error_messages = []

        self.pack()

    def _check_product_entry_validity(self):
        product_entry = self._entry_text.get()
        if product_entry == "Lisää tuote kauppalistalle":
            self._error_messages.append("Kirjoita tuotekenttään tuote.")
            return False
        elif len(product_entry) < 3:
            self._error_messages.append(
                "Kirjoita tuotekenttään tuote, joka on vähintään 3 kirjainta pitkä.")
            return False
        elif len(product_entry) > 30:
            self._error_messages.append(
                "Kirjoita tuotekenttään tuote, joka on enintään 30 kirjainta pitkä.")
            return False
        return True

    def _check_amount_entry_validity(self):
        amount_entry = self._entry_amount.get()
        if amount_entry == 0 or len(amount_entry) == 0:
            self._error_messages.append("Lisää määrä.")
            return False
        try:
            amount_entry = int(amount_entry)
        except:
            self._error_messages.append("Käytä määräkentässä vain numeroita.")
            return False
        return True

    def _check_department_selection_validity(self):
        try:
            self._radiobutton_department.get()
        except:
            self._error_messages.append("Valitse osasto.")
            return False
        return True

    def _find_department_from_selection(self, department_selection: int):
        departments = sorted(
            self._shopping_list_service.get_department_order_in_store())
        return departments[department_selection]

    def _find_selection_from_department(self, searched_department: str):
        departments = sorted(
            self._shopping_list_service.get_department_order_in_store())
        for department in departments:
            if department == searched_department:
                return departments.index(department)
