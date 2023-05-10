from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton
from services.shopping_list_services import ShoppingListService
from entities.product import Product


class EnterItemsFrame:
    """Class responsible for Tkinter-frame with options for searching for products and adding them to shopping list

    Attributes:
        shopping_list_service: service class that controls the application logic
        frame: the master frame of the Tkinter-window into which the user interface is initialized
        suggestions: suggestions for user when product entered incorrectly or product not found
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
        self._suggestions = []
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
        product_entry = ttk.Entry(
            master=self._entry_frame, textvariable=self._entry_text)
        product_entry.grid(row=0, column=0)
        # self._entry_text.insert(0, "Lisää tuote kauppalistalle")

        self._entry_amount = StringVar()
        amount_entry = ttk.Entry(
            master=self._entry_frame, textvariable=self._entry_amount)
        amount_entry.grid(row=0, column=1)
        self._entry_amount.set(0)

        self._option_unit = StringVar()
        unit_options = ["kpl", "ml", "l", "g", "kg"]
        unit_option = ttk.OptionMenu(
            self._entry_frame, self._option_unit, unit_options[0], *unit_options)
        unit_option.grid(row=0, column=2)

        search_product_button = ttk.Button(
            master=self._entry_frame, text="Etsi", command=self._search_product_button_handler)
        search_product_button.grid(row=0, column=3)

        self._entry_frame.pack()

    def _pack_departments_frame(self):
        self._departments_frame = ttk.Frame(master=self._frame)

        self._radiobutton_department = IntVar()
        self._radiobutton_department.set(None)
        departments = sorted(
            self._shopping_list_service.get_department_order_in_store())
        position = 0
        grid_row = 0
        grid_column = 0
        for department in departments:
            department_selection = Radiobutton(
                master=self._departments_frame, text=department.capitalize(), indicatoron=0, variable=self._radiobutton_department, value=position)
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

        for suggestion in self._suggestions:
            product_label = ttk.Label(
                master=self._suggestions_frame, text=suggestion)
            product_label.pack()

        self._suggestions_frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _search_product_button_handler(self):
        self._suggestions = []
        if self._check_product_entry_validity():
            product_suggestion = self._shopping_list_service.find_product(
                self._entry_text.get().lower())
            if product_suggestion[0]:
                product = product_suggestion[1]
                radiobutton_pos = self._find_selection_from_department(
                    product.department)
                self._radiobutton_department.set(radiobutton_pos)
                self._suggestions.append("Tuote löytyi!")
            else:
                self._suggestions = product_suggestion[1]
                suggestion = "Tuotetta ei löytynyt."
                if len(product_suggestion[1]) > 0:
                    suggestion += " Tarkoititko jotain seuraavista?"
                self._suggestions.insert(0, suggestion)

        self._suggestions_frame.destroy()
        self._pack_suggestions_frame()

    def _add_product_button_handler(self):

        self._suggestions = []

        entry_valid = self._check_product_entry_validity()
        amount_valid = self._check_amount_entry_validity()
        department_valid = self._check_department_selection_validity()

        if entry_valid and amount_valid and department_valid:
            amount_entry = int(self._entry_amount.get())
            product_suggestion = self._shopping_list_service.find_product(
                self._entry_text.get())
            if product_suggestion[0]:
                product = product_suggestion[1]
            else:
                department = self._find_department_from_selection(
                    self._radiobutton_department.get())
                product = self._shopping_list_service.create_new_product(
                    self._entry_text.get(), department)
            self._shopping_list_service.add_product_to_current_shopping_list(
                product, amount_entry, self._option_unit.get())
            self._display_shopping_list_changes()
            self._entry_text.set("")
            self._entry_amount.set("")
            self._option_unit.set("kpl")
            self._radiobutton_department.set(None)

        self._suggestions_frame.destroy()
        self._pack_suggestions_frame()

    def _check_product_entry_validity(self):
        product_entry = self._entry_text.get()
        if product_entry == "Lisää tuote kauppalistalle":
            self._suggestions.append("Kirjoita tuotekenttään tuote.")
            return False
        elif len(product_entry) < 3:
            self._suggestions.append(
                "Kirjoita tuotekenttään tuote, joka on vähintään 3 kirjainta pitkä.")
            return False
        return True

    def _check_amount_entry_validity(self):
        amount_entry = self._entry_amount.get()
        try:
            int(amount_entry)
        except:
            self._suggestions.append("Käytä määräkentässä vain numeroita.")
            return False
        return True

    def _check_department_selection_validity(self):
        try:
            self._radiobutton_department.get()
        except:
            self._suggestions.append("Valitse osasto.")
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
