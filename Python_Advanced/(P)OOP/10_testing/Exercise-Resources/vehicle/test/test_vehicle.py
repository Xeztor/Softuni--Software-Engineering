import unittest

from vehicle.project.vehicle import Vehicle


# For Judge
# from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(50, 100)

    def test_vehicle_drive_when_fuel_is_enough__expect_fuel_reduced(self):
        self.car.drive(40)
        self.assertEqual(0, self.car.fuel)

    def test_vehicle_drive_when_fuel_is_not_enough__expect_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(100)

        self.assertEqual('Not enough fuel', str(exc.exception))

    def test_vehicle_refuel_when_fuel_is_not_too_much__expect_tank_to_fill(self):
        self.car.drive(40)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel)

    def test_vehicle_refuel_when_fuel_is_too_much__expect_tank_to_fill(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(100)

        self.assertEqual("Too much fuel", str(exc.exception))

    def test_vehicle_str__expect_message(self):
        self.assertEqual(f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} fuel left "
                         f"and {self.car.fuel_consumption} fuel consumption",
                         str(self.car))


if __name__ == '__main__':
    unittest.main()
