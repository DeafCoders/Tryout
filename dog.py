from random import choice


class Dog:
    crunchies = ["snoep", "koekje", "cake", "pizza"]
    fluids = ["kraanwater", "bier", "regenwater"]

    def __init__(self, name):
        self.Dog = name

    def bark(self):
        return self.Dog + " blaft: \"Woef\" "

    def get_food(self):
        return self.Dog + " eet een " + choice(self.crunchies) + "."

    def do_math(self, first_number, second_number):
        barks = self.bark()[:-2]
        answer = first_number * second_number
        for i in range(1, answer):
            barks += ", woef"
        barks += "!\" (" + str(answer) + "x geblaft)"
        return barks

    def go_racing(self):
        return self.Dog + " is aan het rennen."

    def drink(self):
        return self.Dog + " drinkt " + choice(self.fluids) + "."
