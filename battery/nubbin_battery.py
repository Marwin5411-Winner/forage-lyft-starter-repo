from battery.battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date


    def need_service(self):
        return (self.current_date.year - self.last_service_date.year) > 2
