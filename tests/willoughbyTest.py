import unittest
from engines.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(current_mileage=120000, last_service_mileage=60000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(current_mileage=90000, last_service_mileage=60000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
