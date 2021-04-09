import unittest

from mammal.project.mammal import Mammal

# for judge
# from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    name = 'gosho'
    type = 'felines'
    sound = 'malo'

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_mammal_make_sound__expect_return_message(self):
        actual = self.mammal.make_sound()
        self.assertEqual(f"{self.name} makes {self.sound}", actual)

    def test_mammal_get_kingdom__expect_return_kingdom(self):
        actual = self.mammal.get_kingdom()

        self.assertEqual('animals', actual)

    def test_mammal_info__expect_return_message(self):
        actual = self.mammal.info()

        self.assertEqual(f"{self.name} is of type {self.type}", actual)


if __name__ == '__main__':
    unittest.main()
