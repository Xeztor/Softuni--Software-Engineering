from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    capacity = 50

    def __init__(self, name):
        super().__init__(name, FreshwaterAquarium.capacity)
