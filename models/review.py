#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self,id, user, place, text, rating):
        super().__init__()
        self.id = id
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
