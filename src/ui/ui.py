from tkinter import Tk, ttk, constants, StringVar, IntVar, Radiobutton

from services.shopping_list_services import ShoppingListService
from repositories.product_repository import ProductRepository
from repositories.store_repository import StoreRepository

from ui.options_frame import OptionsFrame
from ui.shopping_list_frame import ShoppingListFrame
from ui.enter_items_frame import EnterItemsFrame


class MainView:
    def __init__(self, root):
        self._shopping_list_service = ShoppingListService(
            ProductRepository(), StoreRepository())
        self._root = root
        self._options_frame = None
        self._shopping_list_frame = None
        self._enter_items_frame = None

    def display(self):

        self._options_frame = OptionsFrame(
            self._root, self._shopping_list_service)
        self._options_frame.pack()

        self._shopping_list_frame = ShoppingListFrame(
            self._root, self._shopping_list_service)
        self._shopping_list_frame.pack()

        self._enter_items_frame = EnterItemsFrame(
            self._root, self._shopping_list_service, self._shopping_list_frame.pack)
        self._enter_items_frame.pack()
