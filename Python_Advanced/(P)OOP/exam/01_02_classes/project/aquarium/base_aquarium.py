from abc import ABC

from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def __str__(self):
        return f"{self.name}:\n" \
               f"Fish: {' '.join(fish.name for fish in self.fish) if self.fish else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}\n"

    @property
    def space_left(self):
        return self.capacity - len(self.fish)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish: BaseFish):
        if not self.space_left:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.__class__.__name__}."

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def feed(self):
        for fish in self.fish:
            fish.eat()
