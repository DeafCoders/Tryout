from random import choice


class Dog:
    __crunchies = ["snoep", "koekje", "cake", "pizza", "niet"]
    __fluids = ["kraanwater", "bier", "regenwater", "niet"]

    def __init__(self, name):
        self.__Dog = name

    def bark(self):
        return self.__Dog + " blaft: \"Woef\" "

    def get_food(self):
        crunchy = choice(self.__crunchies)
        if crunchy == "niet":
            return self.__Dog + " eet " + crunchy + "."
        return self.__Dog + " eet een " + crunchy + "."

    def do_math(self, first_number, second_number):
        barks = self.bark()[:-2]
        answer = first_number * second_number
        if 0 < answer <= 25:
            for i in range(1, answer):
                barks += ", woef"
            barks += "!\" (" + str(answer) + "x geblaft)"
            return barks
        elif answer == 0:
            return self.__Dog + " zwijgt... (" + str(answer) + "x geblaft)"
        else:
            return self.__Dog + " gromt boos: Grrrr! (Je hond wil niet " + str(
                answer) + "x blaffen, graag tussen 0x en 25x)"

    def go_racing(self):
        return self.__Dog + " is aan het rennen."

    def get_drink(self):
        return self.__Dog + " drinkt " + choice(self.__fluids) + "."

    def seek_choice(self):
        for item in self.__crunchies:
            for item in self.__fluids:
                if item == "bier":
                    return item
            if item == "pizza":
                return item
