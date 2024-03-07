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
        self.assertTrue(hasattr(FileStorage, "__file_path"))
        self.assertTrue(hasattr(FileStorage, "__objects"))
        file1 = FileStorage()
        self.assertTrue(hasattr(file1, "__file_path"))
        self.assertTrue(hasattr(file1, "__objects"))
        self.assertTrue(f"{file1.__class__.__name__}.{file1.id}" in FileStorage.__objects.keys())

    def test_all(self):
        """ Test the public instance method "all"
        """
        file2 = FileStorage()
        self.assertEqual(file2.all().__class__.__name__, "dict")
        self.assertEqual(file2.all(), FileStorage.__objects)

    def test_new(self):
        """ Test the public instance method "new"
        """
        file3 = FileStorage()
        self.assertTrue(f"{file3.__class__.__name__}.{file3.id}" in FileStorage.__objects.keys())
        
    def test_save(self):
        """ Test the public instance method "save"
        """
        file4 = FileStorage()
        FileStorage.__file_path = "file.json"
        file4.save()
        with open("file.json", mode="r", encoding="utf-8") as fp:
            self.assertTrue(f"{file4.__class__.__name__}.{file4.id}" in [key for key in json.load(fp)])
        file5 = FileStorage()
        file6 = FileStorage()
        file5.save()
        file6.save()
        with open("file.json", mode="r", encoding="utf-8") as fp:
            self.assertTrue(f"{file4.__class__.__name__}.{file4.id}" in [key for key in json.load(fp)])
            self.assertTrue(f"{file5.__class__.__name__}.{file5.id}" in [key for key in json.load(fp)])
            self.assertTrue(f"{file6.__class__.__name__}.{file6.id}" in [key for key in json.load(fp)])

    def test_reload(self):
        """ Test the public instance method "reload"
        """
        FileStorage.__file_path = "files.json"
        file7 = FileStorage()
        file8 = FileStorage()
        file9 = FileStorage()
        file7.save()
        file8.save()
        file9.save()
        FileStorage.__objects = {}
        file9.reload()
        if os.path.isfile(FileStorage.__file_path):
            self.assertTrue(f"{file7.__class__.__name__}.{file7.id}" in [key for key in FileStorage.__objects])
            self.assertTrue(f"{file8.__class__.__name__}.{file8.id}" in [key for key in FileStorage.__objects])
            self.assertTrue(f"{file9.__class__.__name__}.{file9.id}" in [key for key in FileStorage.__objects])
