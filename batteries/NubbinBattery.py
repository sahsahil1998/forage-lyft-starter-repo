from datetime import date, timedelta
from batteries.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return (date.today() - self.last_service_date).days > (4 * 365)