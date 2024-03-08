#!/usr/bin/env python3
"""
    Test module for the FileStorage Class of the AirBnB Clone
"""
import datetime
import json
import os.path
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test class for the FileStorage
    """
    def test_attr(self):
        """ Test for the private class attributes
        """
        # Test if private class attributes "file_path" and "objects" exists
        self.assertTrue(hasattr(FileStorage, "__file_path"))
        self.assertTrue(hasattr(FileStorage, "__objects"))
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "__file_path"))
        self.assertTrue(hasattr(storage, "__objects"))
        
        # Test if the class attribute "file_path" is a string
        self.assertEqual(type(storage.__file_path).__name__, "str")

        # Test if the class attribute "objects" is a dictionary
        self.assertEqual(type(storage.__objects).__name__, "dict")

        # Test if the objects dictionary is empty initially
        self.assertEqual(len(storage.__objects), 0)

    def test_all(self):
        """ Test the public instance method "all"
        """
        storage = FileStorage()

        # Test if the method "all" return a dictionary
        self.assertEqual(storage.all().__class__.__name__, "dict")

        # Test if the method "all" return the "object" as a dictionary
        self.assertEqual(storage.all(), FileStorage.__objects)

    def test_new(self):
        """ Test the public instance method "new"
        """
        # create an instance of the BaseModel class
        Base1 = BaseModel()
        
        # Test if the new object "Base1" is inserted into the "__objects" dict
        # Check if the object is inserted with the key: <object class name>.id
        self.assertTrue(f"{Base1.__class__.__name__}.{Base1.id}" in FileStorage.__objects.keys())
        
    def test_save(self):
        """ Test the public instance method "save"
        """
        # Test if all objects in "__objects" is saved to the json file_path
        FileStorage.__file_path = "file.json"
        Base2 = BaseModel()
        Base3 = BaseModel()
        Base4 = BaseModel()
        storage = FileStorage()
        storage.save()
        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as fp:
            file_dict = json.load(fp)
            self.assertTrue(f"{Base2.__class__.__name__}.{Base2.id}" in file_dict)
            self.assertTrue(f"{Base3.__class__.__name__}.{Base3.id}" in file_dict)
            self.assertTrue(f"{Base4.__class__.__name__}.{Base4.id}" in file_dict)
        
        # Test if the ids of the saved objects are same as original objects
            self.assertEqual(file_dict[f"{Base2.__class__.__name__}.{Base2.id}"]["id"], Base2.id)
            self.assertEqual(file_dict[f"{Base3.__class__.__name__}.{Base3.id}"]["id"], Base3.id)
            self.assertEqual(file_dict[f"{Base4.__class__.__name__}.{Base4.id}"]["id"], Base4.id)

    def test_reload(self):
        """ Test the public instance method "reload"
        """
        # Test if all objects saved in file are loaded to __objects
        # If file_path does not exist no object is loaded
        FileStorage.__file_path = "files.json"
        Base5 = BaseModel()  # create new objects and save to file
        Base6 = BaseModel()
        Base7 = BaseModel()
        storage = FileStorage()
        storage.save()
        FileStorage.__objects = {}  # set __object to an empty dictionary
        storage.reload()  # reload objects from file

        # Test if all objects have been reloaded to __objects
        if os.path.isfile(FileStorage.__file_path):
            self.assertTrue(f"{Base5.__class__.__name__}.{Base5.id}" in FileStorage.__objects)
            self.assertTrue(f"{Base6.__class__.__name__}.{Base6.id}" in FileStorage.__objects)
            self.assertTrue(f"{Base7.__class__.__name__}.{Base7.id}" in FileStorage.__objects)
