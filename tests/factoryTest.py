import unittest
from datetime import date
from car_factory import CarFactory
from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

class TestCarFactory(unittest.TestCase):

    def test_create_calliope(self):
        car = CarFactory.create_calliope(
            current_date=date.today(),
            last_service_date=date.today(),
            current_mileage=10000,
            last_service_mileage=0,
            tire_wear_values=[0.1, 0.1, 0.1, 0.1]
        )
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertIsInstance(car.tires, CarriganTire)
        self.assertFalse(car.needs_service())

    def test_create_glissade(self):
        car = CarFactory.create_glissade(
            current_date=date.today(),
            last_service_date=date.today(),
            current_mileage=10000,
            last_service_mileage=0,
            tire_wear_values=[0.5, 0.5, 0.5, 0.5]
        )
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertIsInstance(car.tires, OctoprimeTire)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
