from tires.octoprime_tire import OctoprimeTires
import unittest

class TestOctoprimeTires(unittest.TestCase):
    
        def test_needs_service_true(self):
            tires = OctoprimeTires([0.9, 0.9, 0.9, 0.9])
            self.assertTrue(tires.needs_service())
        
        def test_needs_service_false(self):
            tires = OctoprimeTires([0.9, 0.9, 0.9, 0.8])
            self.assertFalse(tires.needs_service())