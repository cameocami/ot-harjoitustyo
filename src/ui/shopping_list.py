from tkinter import Tk, ttk
from services.shopping_list_services import shopping_list_service


class List_frame:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._shopping_list = shopping_list_service.get_shopping_list()

        for item, attributes in self._shopping_list.items():
            label1 = ttk.Label(master=self._frame, text=f'{item}')
            label1.pack()
            label2 = ttk.Label(master=self._frame, text=f'{attributes[0]} {attributes[1]}')
            label2.pack()
            label3 = ttk.Label(master=self._frame, text=f'osasto: {attributes[2]}')
            label3.pack()

    def pack(self):
        self._frame.pack()
            




