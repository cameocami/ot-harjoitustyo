from tkinter import Tk, ttk
from ui.shopping_list import List_frame
from ui.enter_items import Enter_items_frame


class UI:
    def __init__(self, root):
        self._root = root

    def display(self):
        list_frame = List_frame(self._root)
        enter_items_frame = Enter_items_frame(self._root)

        list_frame.pack()
        enter_items_frame.pack()




