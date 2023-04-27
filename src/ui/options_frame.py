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

    def pack(self):
        """Creates the elements in the options frame and displays them."""
        self._compile_shopping_list_button = ttk.Button(
            master=self._frame, text="Laadi kauppalista", command=self._compile_shopping_list_button_handler)
        self._compile_shopping_list_button.grid(
            row=0, column=0, padx=5, pady=5, sticky=constants.E)
        self._frame.pack()

    def destroy(self):
        """Destroys the frame."""
        self._frame.destroy()

    def _compile_shopping_list_button_handler(self):
        """Calls the application logic to compile the shopping list into a new file."""

        self._shopping_list_service.compile_shopping_list()
