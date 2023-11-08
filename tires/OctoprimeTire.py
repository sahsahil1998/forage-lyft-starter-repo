from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_values):
        self.wear_values = wear_values

    def needs_service(self):
        return sum(self.wear_values) >= 3