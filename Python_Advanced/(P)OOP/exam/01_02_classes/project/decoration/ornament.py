from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    comfort = 1
    price = 5

    def __init__(self):
        super().__init__(Ornament.comfort, Ornament.price)
