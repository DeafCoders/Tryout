from dog import Dog
from unittest import *


class DogUnitTest(TestCase):
    """Unit testing class Dog"""

    name = "Hondje"
    dog = Dog(name)

    def test_bark(self):
        text = self.dog.bark()
        self.assertEqual(self.name + " blaft: \"Woef\" ", text)
        # print(text)

    def test_get_food(self):
        text = self.dog.get_food()
        self.assertTrue(text.startswith(self.name + " eet een "))
        # print(text)

    def test_do_math(self):
        text = self.dog.do_math(4, 3)
        self.assertEqual(12, text.lower().count("woef"))
        # print(text)

    def test_go_racing(self):
        text = self.dog.go_racing()
        self.assertEqual(self.name + " is aan het rennen.", text)
        # print(text)

    def test_drink(self):
        text = self.dog.drink()
        self.assertTrue(text.startswith(self.name + " drinkt "))
        # print(text)

if __name__ == '__main__':
    main()
