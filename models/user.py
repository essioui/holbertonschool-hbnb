#!/usr/bin/python3
from models.base_model import base_model
"""
"""

class User(base_model):
    def __init__(self, email, password, first_name, last_name):
        super().__int__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
