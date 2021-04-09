import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTests(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('ssd', 'heavy', 100, 100)

    def test_hardware_install__expect_to_be_installed(self):
        software = Software('test', 'light', 50, 50)
        self.hardware.install(software)

        self.assertEqual([software], self.hardware.software_components)

    def test_hardware_install_when_not_enough_memory__expect_exception(self):
        software = Software('test', 'light', 50, 150)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install_when_not_enough_capacity__expect_exception(self):
        software = Software('test', 'light', 150, 50)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_uninstall__expect_software_removed_from_list(self):
        software = Software('test', 'light', 50, 50)
        self.hardware.install(software)
        self.hardware.uninstall(software)

        self.assertEqual([], self.hardware.software_components)

    def test_hardware_uninstall_when_not_existing_software__expect_none(self):
        software = Software('test', 'light', 150, 50)
        actual = self.hardware.uninstall(software)
        self.assertEqual(None, actual)


if __name__ == '__main__':
    unittest.main()
