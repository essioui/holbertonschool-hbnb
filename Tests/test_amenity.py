#/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(name="Swimming Pool")
    
    def test_amenity_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
    
    def test_amenity_inherits_base_model(self):
        self.assertIsInstance(self.amenity, BaseModel)
    
    def test_amenity_attributes(self):
        self.assertEqual(self.amenity.name, "Swimming Pool")

if __name__ == '__main__':
    unittest.main()
