from tkinter import ttk, constants
from services.shopping_list_services import ShoppingListService


class OptionsFrame:
    """Class responsible for Tkinter-frame of with main options for the user.

    Attributes:
        shopping_list_service: service class that controls the application logic
        frame: the master frame of the Tkinter-window into which the user interface is initialized
        compile_shopping_list_button: Tkinter-button that compiles the shopping list into a new file
    """

    def __init__(self, root, shopping_list_service):
        """Class constructor. 

        Args:
            root (Tk): original Tkinter-window into which the user interface is initialized
            shopping_list_service (ShoppingListService): service class that controls the application logic
        """

        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)

        self._compile_shopping_list_button = None
        self._empty_shopping_list_button = None

    def pack(self):
        """Creates the elements in the options frame and displays them."""

        self._form_compile_shopping_list_button()
        self._form_empty_shopping_list_button()

        self._compile_shopping_list_button.grid(row=0, column=0, padx=5)
        self._empty_shopping_list_button.grid(row=0, column=2)

        self._frame.pack(pady=10)

    def _form_compile_shopping_list_button(self):
        if self._compile_shopping_list_button:
            self._compile_shopping_list_button.destroy()

        self._compile_shopping_list_button = ttk.Button(
            master=self._frame, text="Laadi kauppalista", command=self._compile_shopping_list_button_handler)

    def _form_empty_shopping_list_button(self):
        if self._empty_shopping_list_button:
            self._empty_shopping_list_button.destroy()

        self._empty_shopping_list_button = ttk.Button(
            master=self._frame, text="Tyhjennä kauppalista", command=self._empty_shopping_list_button_handler)

    def destroy(self):
        """Destroys the frame."""
        self._frame.destroy()

    def _compile_shopping_list_button_handler(self):
        """Calls the application logic to compile the shopping list into a new file."""

        self._shopping_list_service.compile_shopping_list_file()
        self._shopping_list_service.open_shopping_list_file()

    def _empty_shopping_list_button_handler(self):
        """Calls the application logic to empty the shopping list."""

        self._shopping_list_service.empty_shopping_list()
