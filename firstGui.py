from dog import Dog
from random import choice
from tkinter import *
from validatingEntry import IntegerEntry, MaxLengthEntry


class Gui(Frame):
    """class gui for creating UI frame"""

    colors = ["white", "black", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "brown", "pink", "grey"]

    def __init__(self, parent):
        """initialize gui itself"""
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Test Gui")
        self.pack(fill=BOTH, expand=1)

        self.dog = Dog
        self.name_entry = MaxLengthEntry
        self.first_number_entry = IntegerEntry
        self.second_number_entry = IntegerEntry
        self.text_label = Label
        self.x_label = Label
        self.ok_calc_button = Button
        self.go_racing_button = Button
        self.give_food_button = Button
        self.give_drink_button = Button

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

        # button "Wijzig achtergrondskleur"
        change_button = Button(self.parent, text="Wijzig achtergrondskleur", command=self.change_button_on_click)
        change_button.place(x=50, y=50)

        # entry (textbox) for dog's name input
        self.name_entry = MaxLengthEntry(self.parent, maxlength=30, width=30)
        self.name_entry.place(x=50, y=104)

        # button "OK" for admitting dog's name input
        ok_name_button = Button(self.parent, text="OK", command=self.ok_name_button_on_click, width=10)
        ok_name_button.place(x=300, y=100)

        # label for showing text to user
        self.text_label = Label(self.parent, text="Hoe heet je hond?", background="white", wraplength=400)
        self.text_label.place(x=50, y=204)

        # label "X" between entries for input numbers
        self.x_label = Label(self.parent, text="X", background="white")
        self.x_label.place(x=428, y=54)
        self.x_label.lower()

        # entry for first number input
        self.first_number_entry = IntegerEntry(self.parent, width=2)
        self.first_number_entry.place(x=400, y=54)
        self.first_number_entry.lower()

        # entry for second number input
        self.second_number_entry = IntegerEntry(self.parent, width=2)
        self.second_number_entry.place(x=450, y=54)
        self.second_number_entry.lower()

        # button "OK, reken" for making dog to do math
        self.ok_calc_button = Button(self.parent, text="OK, reken!", command=self.ok_math_button_on_click, width=10)
        self.ok_calc_button.place(x=400, y=100)
        self.ok_calc_button.lower()

        # button "Ga rennen!" for making dog to go racing
        self.go_racing_button = Button(self.parent, text="Ga rennen!", command=self.go_racing_button_on_click, width=10)
        self.go_racing_button.place(x=200, y=150)
        self.go_racing_button.lower()

        # button "Eten!" for giving food to dog
        self.give_food_button = Button(self.parent, text="Eten!", command=self.give_food_button_on_click, width=10)
        self.give_food_button.place(x=300, y=150)
        self.give_food_button.lower()

        # button "Drinken!" for giving drink to dog
        self.give_drink_button = Button(self.parent, text="Drinken!", command=self.give_drink_button_on_click, width=10)
        self.give_drink_button.place(x=400, y=150)
        self.give_drink_button.lower()

    def change_button_on_click(self):
        """button click event of change_button"""
        color = self.random_color(self["background"])
        self.configure(background=color)
        self.text_label.configure(background=color)
        self.x_label.configure(background=color)
        if color == "black":
            self.text_label.configure(foreground="white")
            self.x_label.configure(foreground="white")
        else:
            self.text_label.configure(foreground="black")
            self.x_label.configure(foreground="black")
        print(color)

    def ok_name_button_on_click(self):
        """button click event of ok_name_button"""
        s = self.name_entry.get()
        if s != "":
            self.dog = Dog(s)
            self.text_label.configure(text=self.dog.bark())

            # show components:
            self.x_label.lift()
            self.first_number_entry.lift()
            self.second_number_entry.lift()
            self.ok_calc_button.lift()
            self.go_racing_button.lift()
            self.give_food_button.lift()
            self.give_drink_button.lift()
        else:
            self.text_label.configure(text="Graag een naam van je hond invoeren.")

            # hide components:
            self.x_label.lower()
            self.first_number_entry.lower()
            self.second_number_entry.lower()
            self.ok_calc_button.lower()
            self.go_racing_button.lower()
            self.give_food_button.lower()
            self.give_drink_button.lower()

    def ok_math_button_on_click(self):
        """button click event of ok_math_button"""
        n1 = int(self.first_number_entry.get())
        n2 = int(self.second_number_entry.get())
        self.text_label.configure(text=self.dog.do_math(n1, n2))

    def go_racing_button_on_click(self):
        """button click event of go_racing_button"""
        self.text_label.configure(text=self.dog.go_racing())

    def give_food_button_on_click(self):
        """button click event of give_food_button"""
        self.text_label.configure(text=self.dog.get_food())

    def give_drink_button_on_click(self):
        """button click event of give_drink_button"""
        self.text_label.configure(text=self.dog.get_drink())

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
