#!/usr/bin/env python3
"""
    Test module for the __init__ module that creates a unique FileStorage instance for the application
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os.path
import unittest


class Test__init__(unittest.TestCase):
    """ Test class for the __init__ module
    """
    def test_models_init(self):
        """ Test the init module of the package "model".

            Checks if the objects are reloaded from file on initialization
        """
        FileStorage.__file_path = "files.json"
        Base1 = BaseModel()  # create new objects and save to file
        Base2 = BaseModel()
        Base3 = BaseModel()
        storage = FileStorage()
        storage.save()

        FileStorage.__objects = {}  # set __objects to empty dictionary

        # Test if variable storage is created on importing __init__ module
        import models.__init__
        self.assertTrue(hasattr(models.__init__, "storage"))

        # Test if variable storage is an instance of FileStorage
        self.assertIsInstance(models.__init__.storage, FileStorage)

        # Test if the objects were reloaded from file to __objects
        if os.path.isfile(FileStorage.__file_path):
            self.assertIn(f"{Base1.__class__.__name__}.{Base1.id}" in FileStorage.__objects)
            self.assertIn(f"{Base2.__class__.__name__}.{Base2.id}", FileStorage.__objects)
            self.assertIn(f"{Base3.__class__.__name__}.{Base3.id}", FileStorage.__objects)
