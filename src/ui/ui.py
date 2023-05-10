from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton

from services.shopping_list_services import ShoppingListService
from repositories.product_repository import ProductRepository
from repositories.store_repository import StoreRepository
from repositories.shopping_list_repository import ShoppingListRepository

from ui.options_frame import OptionsFrame
from ui.shopping_list_frame import ShoppingListFrame
from ui.enter_items_frame import EnterItemsFrame


class MainView:
    """Class responsible for the main user interface of the application.

    Attributes:
        shopping_list_service: service class that controls the application logic
        root: Tkinter-window into which the user interface is initialized
        options_frame: Tkinter-frame with some main options for user
        shopping_list_frame: Tkinter-frame with view of current shopping list
        enter_items_frame: Tkinter-frame with options for searching for products and adding them to shopping list

    """

    def __init__(self, root):
        """Class constructor.

        Args:
            root (Tk): Tkinter-window into which the user interface is initialized 
        """
        self._shopping_list_service = ShoppingListService(
            ProductRepository(), StoreRepository(), ShoppingListRepository())
        self._root = root
        self._options_frame = None
        self._shopping_list_frame = None
        self._enter_items_frame = None

    def display(self):
        """ Displays the mainview."""

        self._options_frame = OptionsFrame(
            self._root, self._shopping_list_service)
        self._options_frame.pack()

        self._shopping_list_frame = ShoppingListFrame(
            self._root, self._shopping_list_service)
        self._shopping_list_frame.pack()

        self._enter_items_frame = EnterItemsFrame(
            self._root, self._shopping_list_service, self._shopping_list_frame.pack)
        self._enter_items_frame.pack()
