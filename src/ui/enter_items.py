from tkinter import ttk

class Enter_items_frame:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)

        self._entry = ttk.Entry(master=self._root)
        self._entry.pack()

        button = ttk.Button(
          master=self._root,
          text="Lisää",
          command=self._handle_button_click
        )

        button.pack()

    def _handle_button_click(self):
        entry_value = self._entry.get()
        print(f"Tuote on: {entry_value}")
            
    def pack(self):
        self._frame.pack()
            