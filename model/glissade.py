from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine

class Glissade(WilloughbyEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)

    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
