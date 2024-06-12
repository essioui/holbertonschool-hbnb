#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            user_id=1,
            city_id=101,
            name="Beautiful Apartment",
            latitude=40.7128,
            longitude=-74.0060,
            host="Alice",
            description="A lovely place in the city center.",
            number_rooms=3,
            number_bathrooms=2,
            max_guest=5,
            price_per_night=150
        )
    
    def test_place_instance(self):
        self.assertIsInstance(self.place, Place)
    
    def test_place_inherits_base_model(self):
        self.assertIsInstance(self.place, BaseModel)
    
    def test_place_attributes(self):
        self.assertEqual(self.place.user_id, 1)
        self.assertEqual(self.place.city_id, 101)
        self.assertEqual(self.place.name, "Beautiful Apartment")
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.host, "Alice")
        self.assertEqual(self.place.description, "A lovely place in the city center.")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_per_night, 150)
        self.assertEqual(self.place.amenities, [])
        self.assertEqual(self.place.reviews, [])
    
    def test_add_amenity(self):
        self.place.add_amenity("WiFi")
        self.assertIn("WiFi", self.place.amenities)
        self.place.add_amenity("WiFi")
        self.assertEqual(len(self.place.amenities), 1)
    
    def test_add_review(self):
        review = "Great place to stay!"
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)

if __name__ == '__main__':
    unittest.main()
