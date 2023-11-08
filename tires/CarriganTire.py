from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_values):
        self.wear_values = wear_values

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wear_values)
