from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton
from services.shopping_list_services import ShoppingListService
from entities.product import Product


class EnterItemsFrame:
    def __init__(self, root, shopping_list_service: ShoppingListService, display_shopping_list_changes):
        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)
        self._display_shopping_list_changes = display_shopping_list_changes

    def pack(self):

        # Entry frame

        self._entry_frame = ttk.Frame(master=self._frame)

        self._entry_text = StringVar()
        self._product_entry = ttk.Entry(
            master=self._entry_frame, textvariable=self._entry_text)
        self._product_entry.grid(row=0, column=0)
        # self._entry_text.set("Lisää tuote kauppalistalle")

        self._entry_amount = StringVar()
        self._amount_entry = ttk.Entry(
            master=self._entry_frame, textvariable=self._entry_amount)
        self._amount_entry.grid(row=0, column=1)
        self._entry_amount.set(0)

        self._option_unit = StringVar()
        unit_options = ["kpl", "ml", "l", "g", "kg"]
        self._unit_option = ttk.OptionMenu(
            self._entry_frame, self._option_unit, unit_options[0], *unit_options)
        self._unit_option.grid(row=0, column=2)

        self._search_product_button = ttk.Button(
            master=self._entry_frame, text="Etsi", command=self._search_product_button_handler)
        self._search_product_button.grid(row=0, column=3)

        self._entry_frame.pack()

        # Departments frame

        self._departments_frame = ttk.Frame(master=self._frame)

        self._radiobutton_department = IntVar()
        self._radiobutton_department.set(None)
        self._departments = sorted(
            self._shopping_list_service.get_department_order_in_store(), key=lambda x: str(x))
        position = 0
        grid_row = 0
        grid_column = 0
        for department in self._departments:
            department_selection = Radiobutton(
                master=self._departments_frame, text=department, indicatoron=0, variable=self._radiobutton_department, value=position)
            department_selection.grid(row=grid_row, column=grid_column)
            position += 1
            grid_row += 1
            if grid_row % 7 == 0:
                grid_row -= 7
                grid_column += 1

        self._departments_frame.pack()

        # Add product -button frame

        self._add_button_frame = ttk.Frame(master=self._frame)

        self._add_product_button = ttk.Button(
            self._add_button_frame, text="Lisää", command=self._add_product_button_handler)
        self._add_product_button.grid(sticky=constants.E)

        self._add_button_frame.pack()

        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _search_product_button_handler(self):
        product_entry = self._entry_text.get()
        if not self._check_product_entry_validity(product_entry):
            raise ValueError("Product name input incorrect")
        product = self._shopping_list_service.find_product(product_entry)
        if product:
            radiobutton_pos = self._find_selection_from_department(
                product.department)
            self._radiobutton_department.set(radiobutton_pos)
        else:
            self._radiobutton_department.set(None)

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

        product = self._shopping_list_service.find_product(product_entry)
        amount_entry = int(amount_entry)
        if product:
            self._shopping_list_service.add_product_to_current_shopping_list(
                product, amount_entry, unit_option)
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

    def _check_product_entry_validity(self, product_entry):
        return True

    def _check_amount_entry_validity(self, amount_entry):
        return True

    def _check_department_selection_validity(self, department_selection):
        return True

    def _find_department_from_selection(self, department_selection):
        return self._departments[department_selection]

    def _find_selection_from_department(self, department_name):
        for department in self._departments:
            if department.name == department_name:
                return self._departments.index(department)
