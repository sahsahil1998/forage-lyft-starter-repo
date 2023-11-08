from serviceable import Serviceable
from engines.engine import Engine
from batteries.battery import Battery
from tires.tire import Tire

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tire):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
