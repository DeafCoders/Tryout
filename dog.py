from random import choice


class Dog:
    crunchies = ["snoep", "koekje", "cake", "pizza", "niet"]
    fluids = ["kraanwater", "bier", "regenwater", "niet"]

    def __init__(self, name):
        self.Dog = name

    def bark(self):
        return self.Dog + " blaft: \"Woef\" "

    def get_food(self):
        return self.Dog + " eet een " + choice(self.crunchies) + "."

    def do_math(self, first_number, second_number):
        barks = self.bark()[:-2]
        answer = first_number * second_number
        if 0 < answer <= 25:
            for i in range(1, answer):
                barks += ", woef"
            barks += "!\" (" + str(answer) + "x geblaft)"
            return barks
        elif answer == 0:
            return self.Dog + " zwijgt... (" + str(answer) + "x geblaft)"
        else:
            return self.Dog + " gromt boos: Grrrr! (Je hond wil niet " + str(answer) + "x blaffen, graag tussen 0x en 25x)"


    def go_racing(self):
        return self.Dog + " is aan het rennen."

    def get_drink(self):
        return self.Dog + " drinkt " + choice(self.fluids) + "."
