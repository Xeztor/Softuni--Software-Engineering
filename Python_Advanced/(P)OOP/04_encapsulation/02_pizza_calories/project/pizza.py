from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value: int):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value: dict):
        self.__toppings = value

    def add_topping(self, topping: Topping):
        if not self.is_space_for_topping_left():
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        all_toppings_wights = [weight for weight in self.toppings.values()]
        return sum(all_toppings_wights) + self.dough.weight

    def is_space_for_topping_left(self):
        return self.toppings_capacity > len(self.toppings)
