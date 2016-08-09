from dog import Dog
from random import choice
from tkinter import *
from validatingEntry import IntegerEntry, MaxLengthEntry


class Gui(Frame):
    """class gui for creating UI frame"""

    __colors = ["white", "black", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "brown", "pink", "grey"]

    def __init__(self, parent):
        """initialize gui itself"""
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Test Gui")
        self.pack(fill=BOTH, expand=1)

        self.__dog = Dog
        self.__name_entry = MaxLengthEntry
        self.__first_number_entry = IntegerEntry
        self.__second_number_entry = IntegerEntry
        self.__text_label = Label
        self.__x_label = Label
        self.__ok_calc_button = Button
        self.__go_racing_button = Button
        self.__give_food_button = Button
        self.__give_drink_button = Button

        self.__center_window()
        self.__init_ui()

    def __center_window(self):
        """define position and size of gui"""
        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def __init_ui(self):
        """initialize UI components"""

        # button "Wijzig achtergrondskleur"
        change_button = Button(self.parent, text="Wijzig achtergrondskleur", command=self.__change_button_on_click)
        change_button.place(x=50, y=50)

        # entry (textbox) for dog's name input
        self.__name_entry = MaxLengthEntry(self.parent, maxlength=30, width=30)
        self.__name_entry.place(x=50, y=104)

        # button "OK" for admitting dog's name input
        ok_name_button = Button(self.parent, text="OK", command=self.__ok_name_button_on_click, width=10)
        ok_name_button.place(x=300, y=100)

        # label for showing text to user
        self.__text_label = Label(self.parent, text="Hoe heet je hond?", background="white", wraplength=400)
        self.__text_label.place(x=50, y=204)

        # label "X" between entries for input numbers
        self.__x_label = Label(self.parent, text="X", background="white")
        self.__x_label.place(x=428, y=54)
        self.__x_label.lower()

        # entry for first number input
        self.__first_number_entry = IntegerEntry(self.parent, width=2)
        self.__first_number_entry.place(x=400, y=54)
        self.__first_number_entry.lower()

        # entry for second number input
        self.__second_number_entry = IntegerEntry(self.parent, width=2)
        self.__second_number_entry.place(x=450, y=54)
        self.__second_number_entry.lower()

        # button "OK, reken!" for making dog to do math
        self.__ok_calc_button = Button(self.parent, text="OK, reken!", command=self.__ok_math_button_on_click, width=10)
        self.__ok_calc_button.place(x=400, y=100)
        self.__ok_calc_button.lower()

        # button "Ga rennen!" for making dog to go racing
        self.__go_racing_button = Button(self.parent, text="Ga rennen!", command=self.__go_racing_button_on_click, width=10)
        self.__go_racing_button.place(x=200, y=150)
        self.__go_racing_button.lower()

        # button "Eten!" for giving food to dog
        self.__give_food_button = Button(self.parent, text="Eten!", command=self.__give_food_button_on_click, width=10)
        self.__give_food_button.place(x=300, y=150)
        self.__give_food_button.lower()

        # button "Drinken!" for giving drink to dog
        self.__give_drink_button = Button(self.parent, text="Drinken!", command=self.__give_drink_button_on_click, width=10)
        self.__give_drink_button.place(x=400, y=150)
        self.__give_drink_button.lower()

    def __change_button_on_click(self):
        """button click event of change_button"""
        color = self.__random_color(self["background"])
        self.configure(background=color)
        self.__text_label.configure(background=color)
        self.__x_label.configure(background=color)
        if color == "black":
            self.__text_label.configure(foreground="white")
            self.__x_label.configure(foreground="white")
        else:
            self.__text_label.configure(foreground="black")
            self.__x_label.configure(foreground="black")
        print(color)

    def __ok_name_button_on_click(self):
        """button click event of ok_name_button"""
        s = self.__name_entry.get()
        if s != "":
            self.__dog = Dog(s)
            self.__text_label.configure(text=self.__dog.bark())

            # show components:
            self.__x_label.lift()
            self.__first_number_entry.lift()
            self.__second_number_entry.lift()
            self.__ok_calc_button.lift()
            self.__go_racing_button.lift()
            self.__give_food_button.lift()
            self.__give_drink_button.lift()
        else:
            self.__text_label.configure(text="Graag een naam van je hond invoeren.")

            # hide components:
            self.__x_label.lower()
            self.__first_number_entry.lower()
            self.__second_number_entry.lower()
            self.__ok_calc_button.lower()
            self.__go_racing_button.lower()
            self.__give_food_button.lower()
            self.__give_drink_button.lower()

    def __ok_math_button_on_click(self):
        """button click event of ok_math_button"""
        n1 = int(self.__first_number_entry.get())
        n2 = int(self.__second_number_entry.get())
        self.__text_label.configure(text=self.__dog.do_math(n1, n2))

    def __go_racing_button_on_click(self):
        """button click event of go_racing_button"""
        self.__text_label.configure(text=self.__dog.go_racing())

    def __give_food_button_on_click(self):
        """button click event of give_food_button"""
        self.__text_label.configure(text=self.__dog.get_food())

    def __give_drink_button_on_click(self):
        """button click event of give_drink_button"""
        self.__text_label.configure(text=self.__dog.get_drink())

    def __random_color(self, old_color):
        """get different color"""
        new_color = old_color
        while new_color == old_color:
            new_color = choice(self.__colors)
        return new_color


def __main():
    """testing gui manipulation"""
    root = Tk()
    Gui(root)
    root.mainloop()


if __name__ == '__main__':
    __main()
