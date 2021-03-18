from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, price, milliliters):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.milliliters = milliliters
        self.caffeine = float
