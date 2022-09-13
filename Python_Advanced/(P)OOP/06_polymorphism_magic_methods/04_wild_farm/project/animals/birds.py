from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    WEIGHT_GAIN = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.get_class_name()} does not eat {type(food).__name__}!"

        self.gain_weight(self.WEIGHT_GAIN, food)


class Hen(Bird):
    WEIGHT_GAIN = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(self.WEIGHT_GAIN, food)
