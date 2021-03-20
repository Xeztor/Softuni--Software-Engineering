from project.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += 0.9

    def drive(self, distance):
        if distance * self.fuel_consumption > self.fuel_quantity:
            return

        self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel
