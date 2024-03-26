import unittest

from tire import octoprime_tire

class CarriganTireTest(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        wear_array = [0.1, 0.1, 0.9, 0.1]
        tire = octoprime_tire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_array = [0.1, 0.1, 0.1, 0.1]
        tire = octoprime_tire(wear_array)
        self.assertFalse(tire.needs_service())