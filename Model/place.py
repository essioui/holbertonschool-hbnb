#!/usr/bin/python3
import uuid
from datetime import datetime

class Place:
    def __init__(self, user_id, city_id, name, description, number_rooms, number_bathrooms, max_guest, price_per_night):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.city_id = city_id
        self.name = name
        self.description = description
        self.number_rooms = number_bathrooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        self.amenities = []
        