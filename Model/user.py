#!/usr/bin/python3
import uuid
from datetime import datetime


class User:
    def __init__(self, email, password, first_name, last_name):
        self.id = uuid.uuid4()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.update_at = datetime.now()

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, first_name={self.first_name}, last_name={self.last_name})"
