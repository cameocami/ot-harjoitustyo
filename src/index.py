from tkinter import Tk
from ui.ui import MainView


def main():

    window = Tk()
    window.title("Kauppalista")

    ui_view = MainView(window)
    ui_view.display()

    window.bind(
        '<Return>', lambda event: ui_view.enter_items_frame.search_product_button_handler())
    window.bind('<Control-Return>',
                lambda event: ui_view.enter_items_frame.add_product_button_handler())

    window.mainloop()


if __name__ == "__main__":
    main()
