from tkinter import ttk, constants
from services.shopping_list_services import ShoppingListService


class ShoppingListFrame:
    """Class responsible for Tkinter-frame of with a view of the current shopping list.

    Attributes:
        shopping_list_service: service class that controls the application logic
        frame: the master frame of the Tkinter-window into which the user interface is initialized
        current_shopping_list_frame: Tkinter-frame for the view of the current shopping list
    """

    def __init__(self, root, shopping_list_service: ShoppingListService):
        """Class constructor. 

        Args:
            root (Tk): original Tkinter-window into which the user interface is initialized
            shopping_list_service (ShoppingListService): service class that controls the application logic
        """
        self._shopping_list_service = shopping_list_service
        self._frame = ttk.Frame(master=root)
        self._current_shopping_list_frame = None

    def pack(self):
        """Recreates the elements in the shopping list frame and displays them."""
        if self._current_shopping_list_frame:
            self._current_shopping_list_frame.destroy()
        self._current_shopping_list_frame = ttk.Frame(self._frame)

        for product, amounts in self._shopping_list_service.get_current_shopping_list().items():
            product_frame = ttk.Frame(self._current_shopping_list_frame)
            product_label = ttk.Label(master=product_frame, text=str(product))
            product_label.grid(row=0, column=0, padx=5,
                               pady=5, sticky=constants.W)
            rows = 0
            for unit, amount in amounts.items():
                if amount > 0:
                    amount_label = ttk.Label(
                        master=product_frame, text=f'{amount} {unit}')
                    amount_label.grid(row=rows, column=1,
                                      padx=5, pady=5, sticky=constants.W)
                    delete_button = ttk.Button(
                        master=product_frame, text="x", command=lambda arg1=product, arg2=unit: self._delete_button_handler(arg1, arg2))
                    delete_button.grid(row=rows, column=2, padx=5,
                                       pady=5, sticky=constants.W)
                    rows += 1
            product_frame.pack()
        self._current_shopping_list_frame.pack()
        self._frame.pack()

    def _delete_button_handler(self, product, unit):
        self._shopping_list_service.delete_product_from_shopping_list(
            product, unit)
        self.pack()

    def destroy(self):
        """Destroys the frame"""
        self._frame.destroy()
