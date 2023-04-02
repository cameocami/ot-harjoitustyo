from tkinter import Tk, ttk
from ui.shopping_list import List_frame
from ui.enter_items import Enter_items_frame


class UI:
    def __init__(self, root):
        self._root = root

    def display(self):
        main_view = Main_view(self._root)

        main_view.pack()




