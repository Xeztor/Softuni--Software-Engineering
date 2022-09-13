from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


AQUARIUM_CLASSES_NAMES_MAPPER = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
DECORATIONS_CLASSES_NAMES_MAPPER = {"Ornament": Ornament, "Plant": Plant}
FISH_CLASSES_NAMES_MAPPER = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
