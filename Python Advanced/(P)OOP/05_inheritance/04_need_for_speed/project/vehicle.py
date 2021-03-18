class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horsepower):
        self.fuel_consumption = float(self.DEFAULT_FUEL_CONSUMPTION)
        self.fuel = fuel
        self.horse_power = horsepower

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption > self.fuel:
            return

        self.fuel -= kilometers * self.fuel_consumption
