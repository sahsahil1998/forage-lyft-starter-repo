import unittest
from tires.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTire([0.8, 0.8, 0.7, 0.8])  # Sum is 3.1
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTire([0.5, 0.5, 0.5, 0.5])  # Sum is 2.0
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()