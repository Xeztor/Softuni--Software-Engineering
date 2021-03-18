class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val: float):
        self.__price = val
