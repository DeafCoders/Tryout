import random

class Hond:
    brokjes = ["Snoep", "Koekje", "Cake", "Pizza"]

    def __init__(self):
        self.Dog = "Hondje"

    def blaffen(self):
        return self.Dog + " blaft"

    def kiesEten(self):
        return random.choice(self.brokjes)

    def gaRekenen(self, eerstGetal, tweedeGetal):
        return "Woef woef " + str(eerstGetal * tweedeGetal)

    def gaRennen(self):
        return self.Dog + " is aan het rennen."