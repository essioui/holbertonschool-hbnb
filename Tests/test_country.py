#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country(name="CountryName")
    
    def test_country_instance(self):
        self.assertIsInstance(self.country, Country)
    
    def test_country_attributes(self):
        self.assertEqual(self.country.name, "CountryName")
        self.assertEqual(self.country.cities, [])
    
    def test_add_city(self):
        self.country.add_city("City1")
        self.assertIn("City1", self.country.cities)
        self.assertEqual(len(self.country.cities), 1)
        self.country.add_city("City2")
        self.assertIn("City2", self.country.cities)
        self.assertEqual(len(self.country.cities), 2)

if __name__ == '__main__':
    unittest.main()
