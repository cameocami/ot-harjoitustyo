from tkinter import Tk
from ui.shopping_list_ui import Main_View


def main():

    window = Tk()
    window.title("Kauppalista")

    ui_view = MainView(window)
    ui_view.display()

    window.mainloop()


if __name__ == "__main__":
    main()
