#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self,id, user_id, city_id, name, latitude, longitude, host, description, number_rooms, number_bathrooms, max_guest, price_per_night):
        super().__init__()
        self.id = id
        self.user_id = user_id
        self.city_id = city_id
        self.name = name
        self.description = description
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.number_rooms = number_rooms
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)
