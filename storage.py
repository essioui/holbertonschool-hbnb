#!/usr/bin/python3
import json

class Storage:
    """
    Handles the storage of instances of various classes.
    """

    def __init__(self, filename):
        """
        Initialize the storage with the specified filename.

        :param filename: The name of the file to store data.
        """
        self.filename = filename
        self.data = {}

    def save(self):
        """
        Save the data to the file in JSON format.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def load(self):
        """
        Load the data from the file.
        """
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # If file not found, initialize with an empty dictionary
            self.data = {}

    def add_instance(self, instance):
        """
        Add an instance to the storage.

        :param instance: The instance to be added.
        """
        if instance.__class__.__name__ not in self.data:
            self.data[instance.__class__.__name__] = {}
        self.data[instance.__class__.__name__][instance.id] = instance.__dict__

    def get_instance(self, cls, id):
        """
        Get an instance from the storage by class name and ID.

        :param cls: The class name of the instance.
        :param id: The ID of the instance.
        :return: The instance if found, None otherwise.
        """
        if cls.__name__ in self.data and id in self.data[cls.__name__]:
            instance_data = self.data[cls.__name__][id]
            instance = cls(**instance_data)
            return instance
        return None
