from battery.spindler_battery import SpindlerBattery
import unittest

class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_needs_service_true(self):
        battery = SpindlerBattery(self.today, self.today - timedelta(days=300))
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        battery = SpindlerBattery(self.today, self.today - timedelta(days=30))
        self.assertFalse(battery.needs_service())