#!/usr/bin/python3
"""
"""
from models.base_model import base_model

class Review(base_model):

    def __init__(self, user, place, text, rating):
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
