from datetime import date
from cars.car import Car
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery
from batteries.nubbin_battery import NubbinBattery
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTire(tire_wear_values)  # Assuming Calliope uses Carrigan tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTire(tire_wear_values)  # Assuming Glissade uses Octoprime tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_values: list[float]) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTire(tire_wear_values)  # Assuming Palindrome uses Carrigan tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTire(tire_wear_values)  # Assuming Rorschach uses Octoprime tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = CarriganTire(tire_wear_values)  # Assuming Thovex uses Carrigan tires
        return Car(engine, battery, tires)