#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City(name="CityName", country="CountryName")
    
    def test_city_instance(self):
        self.assertIsInstance(self.city, City)
    
    def test_city_inherits_base_model(self):
        self.assertIsInstance(self.city, BaseModel)
    
    def test_city_attributes(self):
        self.assertEqual(self.city.name, "CityName")
        self.assertEqual(self.city.country, "CountryName")

if __name__ == '__main__':
    unittest.main()
