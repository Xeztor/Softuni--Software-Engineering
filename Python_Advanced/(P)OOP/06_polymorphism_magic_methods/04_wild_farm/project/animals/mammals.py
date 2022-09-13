from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_GAIN = 0.1

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and \
                not isinstance(food, Fruit):
            return f"{self.get_class_name()} does not eat {type(food).__name__}!"

        self.gain_weight(self.WEIGHT_GAIN, food)


class Dog(Mammal):
    WEIGHT_GAIN = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.get_class_name()} does not eat {type(food).__name__}!"

        self.gain_weight(self.WEIGHT_GAIN, food)


class Cat(Mammal):
    WEIGHT_GAIN = 0.3

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and \
                not isinstance(food, Meat):
            return f"{self.get_class_name()} does not eat {type(food).__name__}!"

        self.gain_weight(self.WEIGHT_GAIN, food)


class Tiger(Mammal):
    WEIGHT_GAIN = 1.0

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.get_class_name()} does not eat {type(food).__name__}!"

        self.gain_weight(self.WEIGHT_GAIN, food)
