import unittest
from datetime import datetime, timedelta
from batteries.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.today() - timedelta(days=365*5)  # 5 years ago
        battery = NubbinBattery(last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.today() - timedelta(days=365*2)  # 2 years ago
        battery = NubbinBattery(last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
