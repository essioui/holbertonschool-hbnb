#!/usr/bin/python3
from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
