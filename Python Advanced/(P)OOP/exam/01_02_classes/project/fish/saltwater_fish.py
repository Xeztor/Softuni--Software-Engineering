from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)
        self.water_env = SaltwaterAquarium

    def eat(self):
        self.size += 2
