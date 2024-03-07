#!/usr/bin/env python3
"""
    Test module for the __init__ module that creates a unique FileStorage instance for the application
"""
from models.engine.file_storage import FileStorage
import os.path
import unittest


class Test__init__(unittest.TestCase):
    """ Test class for the __init__ module
    """
    def test_models_init(self):
        """ Test the init module of the package "model".

            Checks if the objects are reloaded from file at the start of application
        """
        FileStorage.__file_path = "files.json"
        file7 = FileStorage()
        file8 = FileStorage()
        file9 = FileStorage()
        file7.save()
        file8.save()
        file9.save()
        FileStorage.__objects = {}
        import models.__init__
        self.assertTrue(hasattr(models.__init__, "storage"))
        storage = models.__init__.storage
        self.assertIsInstance(storage, FileStorage)
        if os.path.isfile(FileStorage.__file_path):
            self.assertTrue(f"{storage.__class__.__name__}.{storage.id}" in [key for key in FileStorage.__objects])
            self.assertTrue(f"{file7.__class__.__name__}.{file7.id}" in [key for key in FileStorage.__objects])
            self.assertTrue(f"{file8.__class__.__name__}.{file8.id}" in [key for key in FileStorage.__objects])
            self.assertTrue(f"{file9.__class__.__name__}.{file9.id}" in [key for key in FileStorage.__objects])
