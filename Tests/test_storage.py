#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from storage import Storage
from models.user import User
from models.place import Place
from models.review import Review
from models.country import Country
from models.city import City
from models.amenity import Amenity

class TestStorage(unittest.TestCase):
    TEST_FILE = 'test_data.json'

    def setUp(self):
        # Initialize storage
        self.storage = Storage(filename=self.TEST_FILE)
        # Create test data
        self.user = User(id=1, email="salah@example.com", password="password", first_name="salah", last_name="essioui")
        self.place = Place(id=1, user_id=1, city_id=101, name="Beautiful Apartment", latitude=40.7128, longitude=-74.0060, host="Alice", description="A lovely place in the city center.", number_rooms=3, number_bathrooms=2, max_guest=5, price_per_night=150)
        self.review = Review(id=1, user="user123", place="place123", text="This is a great place!", rating=5)
        self.country = Country(name="CountryName")
        self.city = City(name="CityName", country="CountryName")
        self.amenity = Amenity(name="Swimming Pool")

    def tearDown(self):
        # Remove test file after tests
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_save_load_instance(self):
        # Add instances to storage
        self.storage.add_instance(self.user)
        self.storage.add_instance(self.place)
        self.storage.add_instance(self.review)
        self.storage.add_instance(self.country)
        self.storage.add_instance(self.city)
        self.storage.add_instance(self.amenity)

        # Save data to file
        self.storage.save()

        # Clear data from storage
        self.storage.data = {}

        # Load data from file
        self.storage.load()

        # Check if instances are loaded correctly
        self.assertEqual(self.storage.get_instance(User, 1).__dict__, self.user.__dict__)
        self.assertEqual(self.storage.get_instance(Place, 1).__dict__, self.place.__dict__)
        self.assertEqual(self.storage.get_instance(Review, 1).__dict__, self.review.__dict__)
        self.assertEqual(self.storage.get_instance(Country, 1).__dict__, self.country.__dict__)
        self.assertEqual(self.storage.get_instance(City, 1).__dict__, self.city.__dict__)
        self.assertEqual(self.storage.get_instance(Amenity, 1).__dict__, self.amenity.__dict__)

if __name__ == '__main__':
    unittest.main()
