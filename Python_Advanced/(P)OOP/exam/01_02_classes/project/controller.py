from project.decoration.decoration_repository import DecorationRepository
from project.mappers import DECORATIONS_CLASSES_NAMES_MAPPER, AQUARIUM_CLASSES_NAMES_MAPPER, FISH_CLASSES_NAMES_MAPPER


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @property
    def aquarium_names(self):
        return [aq.name for aq in self.aquariums]

    def add_aquarium(self, aquarium_type, aquarium_name):
        pass
        # if aquarium_type not in AQUARIUM_CLASSES_NAMES_MAPPER:
        #     return "Invalid aquarium type."
        #
        # aquarium_type = AQUARIUM_CLASSES_NAMES_MAPPER[aquarium_type]
        # aquarium = aquarium_type(aquarium_name)
        # self.aquariums.append(aquarium)
        # return f"Successfully added {aquarium_type.__name__}."

    def add_decoration(self, decoration_type):
        if decoration_type not in DECORATIONS_CLASSES_NAMES_MAPPER:
            return "Invalid decoration type."

        decoration_type = DECORATIONS_CLASSES_NAMES_MAPPER[decoration_type]
        decoration = decoration_type()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type.__name__}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        available_decoration = self.decorations_repository.find_by_type(decoration_type)
        if available_decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium_name not in self.aquarium_names:
            return

        aquarium = self.__get_aquarium_by_name(aquarium_name)

        self.decorations_repository.remove(available_decoration)
        aquarium.add_decoration(available_decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in FISH_CLASSES_NAMES_MAPPER:
            return f"There isn't a fish of type {fish_type}."

        type_fish = FISH_CLASSES_NAMES_MAPPER[fish_type]
        fish = type_fish(fish_name, fish_species, price)

        if aquarium_name not in self.aquarium_names:
            return

        aquarium = [aq for aq in self.aquariums if aq.name == aquarium_name].pop()
        if not aquarium.space_left:
            return aquarium.add_fish(fish)

        if fish.water_env is not type(aquarium):
            return "Water not suitable."

        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        if aquarium_name not in self.aquarium_names:
            return

        aquarium = self.__get_aquarium_by_name(aquarium_name)
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        if aquarium_name not in self.aquarium_names:
            return

        aquarium = self.__get_aquarium_by_name(aquarium_name)
        decorations_price = sum([decoration.price for decoration in aquarium.decorations])
        fish_price = sum([fish.price for fish in aquarium.fish])
        value = decorations_price + fish_price

        return f"{value:.2f}"

    def report(self):
        res = ''
        for aq in self.aquariums:
            res += str(aq)

        return res

    def __get_aquarium_by_name(self, name):
        return [aq for aq in self.aquariums if aq.name == name].pop()
