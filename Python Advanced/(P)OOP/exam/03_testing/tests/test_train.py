import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):
    def setUp(self):
        self.train = Train('tomas', 5)

    def test_train_add__expect_passenger_added(self):
        self.train.add('gosho')
        self.assertEqual(['gosho'], self.train.passengers)

    def test_train_add_when_no_capacity__expect_exception(self):
        self.train.capacity = 1
        self.train.add('gosho')
        with self.assertRaises(ValueError) as ex:
            self.train.add('pesho')

        self.assertEqual("Train is full", str(ex.exception))

    def test_train_add_when_passengers_with_same_name__expect_exception(self):
        self.train.add('gosho')
        with self.assertRaises(ValueError) as ex:
            self.train.add('gosho')

        self.assertEqual("Passenger gosho Exists", str(ex.exception))

    def test_train_remove__expect_to_remove_passenger_and_return_msg(self):
        self.train.add('gosho')
        self.assertEqual(['gosho'], self.train.passengers)

        msg = self.train.remove('gosho')
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Removed gosho", msg)

    def test_train_remove_when_non_existing_passenger__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove('gosho')

        self.assertEqual("Passenger Not Found", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
