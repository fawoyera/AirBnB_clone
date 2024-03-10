#!/usr/bin/python3
""" FileStorage Class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel, "User": User, "State": State, "City": City,
    "Amenity": Amenity, "Place": Place, "Review": Review
}


class FileStorage:
    """
    This class handles the serialization and deserialization of
    objects to/from a JSON file.
    """

    # Path to the JSON file (string)
    __file_path = "file.json"

    # Empty dictionary to store all objects by <class name>.id (dict)
    __objects = {}

    # Public instance methodes
    def all(self):
        """
        Returns the dictionary of all serialized objects.

        Returns:
            dict: Dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj: Object to be serialized and stored.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary of objects to JSON format
        and saves it to the file.
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as storage_file:
            json.dump(serialized_objects, storage_file)

    def reload(self):
        """
        Deserializes the JSON file and reloads the dictionary of objects.
        """
        try:
            with open(FileStorage.__file_path, 'r') as storage_file:
                data = json.load(storage_file)

                for key, json_obj in data.items():
                    # Extract class name and object id from the key
                    class_name, obj_id = key.split('.')

                    # Retrieve the class object based on the class name
                    cls = classes[class_name]

                    # Instantiate an object of the retrieved class using
                    # the object's attributes from the JSON data
                    obj = cls(**json_obj)

                    # Store the object in the dictionary of objects
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
