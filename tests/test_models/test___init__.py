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
    # Create and save some objects to file before running tests
    Base11 = BaseModel()
    Base12 = BaseModel()
    Base11.save()
    Base12.save()

    def test_models_init(self):
        """ Test the init module of the package "model".

            Checks if the objects are reloaded from file on initialization
        """
        # Test if the objects are reloaded from file on import of __init__
        import models.__init__
        storage = FileStorage()
        self.assertIn(f"{self.Base11.__class__.__name__}.{self.Base11.id}", storage.all())
        self.assertIn(f"{self.Base12.__class__.__name__}.{self.Base12.id}", storage.all())

        # Create and save objects to file and check if they are reloaded
        FileStorage.__file_path = "files.json"
        Base1 = BaseModel()  # create new objects and save to file
        Base2 = BaseModel()
        Base3 = BaseModel()
        Base1.save()
        Base2.save()
        Base3.save()
        storage = FileStorage()
        storage.save()

        # set __objects to empty dictionary
        FileStorage.__objects = {}

        # Test if variable storage is created on importing __init__ module
        # import models.__init__
        self.assertTrue(hasattr(models.__init__, "storage"))

        # Test if variable storage is an instance of FileStorage
        self.assertIsInstance(models.__init__.storage, FileStorage)

        # Test if the objects were reloaded from file to __objects
        if os.path.isfile(FileStorage.__file_path):
            self.assertIn(f"{Base1.__class__.__name__}.{Base1.id}", FileStorage.__objects)
            self.assertIn(f"{Base2.__class__.__name__}.{Base2.id}", FileStorage.__objects)
            self.assertIn(f"{Base3.__class__.__name__}.{Base3.id}", FileStorage.__objects)
