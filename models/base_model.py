#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):


        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "created_at":
                if isinstance(value, str):
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.created_at = value
            elif key == "updated_at":
                if isinstance(value, str):
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.updated_at = value
            else:
                if key != "__class__":
                    setattr(self, key, value)
