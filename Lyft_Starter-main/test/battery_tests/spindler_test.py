import unittest
from datetime import date
from battery import SpindlerBattery

class Nubbin_Battery_Test(unittest.TestCase):
    def test_need_service_true(self):
        current_date = date.today()
        last_service_date = date.fromisoformat("2020-05-15")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.today()
        last_service_date = date.fromisoformat("2021-03-10")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())