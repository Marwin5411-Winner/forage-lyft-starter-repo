from engine.willoughby_engine import WilloughbyEngine
import unittest

class TestWilloughbyEngine(unittest.TestCase):
    
        def test_needs_service_true(self):
            engine = WilloughbyEngine(100000, 0)
            self.assertTrue(engine.needs_service())
        
        def test_needs_service_false(self):
            engine = WilloughbyEngine(1000, 0)
            self.assertFalse(engine.needs_service())