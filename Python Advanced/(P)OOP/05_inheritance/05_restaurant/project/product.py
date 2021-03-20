class Product:
    def __init__(self, name, price: float):
        self.name = name
        self.price = float(price)

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
