import unittest
from datetime import datetime, timedelta

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCar(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_calliope_needs_service(self):
        car = Car(CapuletEngine(self.today, 10000, 0), SpindlerBattery(self.today, self.today - timedelta(days=300)))
        self.assertFalse(car.needs_service())
    
    def test_glissade_needs_service(self):
        car = Car(WilloughbyEngine(self.today, 10000, 0), SpindlerBattery(self.today, self.today - timedelta(days=300)))
        self.assertFalse(car.needs_service())

    def test_palindrome_needs_service(self):
        car = Car(SternmanEngine(self.today, False), SpindlerBattery(self.today, self.today - timedelta(days=300)))
        self.assertFalse(car.needs_service())

    def test_rorschach_needs_service(self):
        car = Car(WilloughbyEngine(self.today, 1000, 0), NubbinBattery(self.today, self.today - timedelta(days=300)))
        self.assertFalse(car.needs_service())

    def test_thovex_needs_service(self):
        car = Car(CapuletEngine(self.today, 10000, 0), NubbinBattery(self.today, self.today - timedelta(days=300)))
        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()
