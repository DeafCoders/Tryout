from tkinter import *
from random import choice


class Gui(Frame):
    """class gui for creating UI frame"""

    colors = ["white", "black", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "brown", "pink", "grey"]

    def __init__(self, parent):
        """initialize gui itself"""
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Test Gui")
        self.pack(fill=BOTH, expand=1)
        self.center_window()
        self.init_ui()

    def center_window(self):
        """define position and size of gui"""
        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def init_ui(self):
        """initialize UI components"""
        change_button = Button(self.parent, text="Change background color", command=self.change_button_on_click)
        change_button.place(x=50, y=50)

    def change_button_on_click(self):
        """button click event of change_button"""
        color = self.random_color(self["background"])
        self.configure(background=color)
        print(color)

    def random_color(self, old_color):
        """get different color"""
        new_color = old_color
        while new_color == old_color:
            new_color = choice(self.colors)
        return new_color


def main():
    """testing gui manipulation"""
    root = Tk()
    Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
