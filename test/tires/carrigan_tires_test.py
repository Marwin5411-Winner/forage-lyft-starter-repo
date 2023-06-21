from tires.carrigan_tire import CarriganTires
import unittest

class TestCarriganTires(unittest.TestCase):

    def test_needs_service_true(self):
        tires = CarriganTires([0.9, 0.9, 0.9, 0.9])
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tires = CarriganTires([0.9, 0.9, 0.9, 0.8])
        self.assertFalse(tires.needs_service())
    