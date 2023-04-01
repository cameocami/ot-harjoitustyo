from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Kauppalista")

    ui_view = UI(window)
    ui_view.display()

    window.mainloop()


if __name__ == "__main__":
    main()