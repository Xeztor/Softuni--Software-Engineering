from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def gain_weight(self, weight_gain, food):
        self.food_eaten += food.quantity
        self.weight += weight_gain * food.quantity


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.get_class_name()} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.get_class_name()} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass
