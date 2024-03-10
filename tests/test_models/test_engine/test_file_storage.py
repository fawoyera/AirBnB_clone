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
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Test class for the FileStorage
    """
    def test_attr(self):
        """ Test for the private class attributes
        """
        # Test if private class attributes "file_path" and "objects" exists
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        storage = FileStorage()
        storage.reload()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

        # Test if the class attribute "file_path" is a string
        self.assertEqual(type(storage._FileStorage__file_path).__name__,
                         "str")

        # Test if the class attribute "objects" is a dictionary
        self.assertEqual(type(storage._FileStorage__objects).__name__,
                         "dict")

    def test_all(self):
        """ Test the public instance method "all"
        """
        Base1 = BaseModel()
        Base2 = BaseModel()
        Base1.save()
        Base2.save()
        storage = FileStorage()

        # Test if the method "all" return a dictionary
        self.assertEqual(storage.all().__class__.__name__, "dict")

        # Test if the method "all" return the "object" as a dictionary
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new(self):
        """ Test the public instance method "new"
        """
        from models import storage

        # create an instance of the BaseModel class
        Base1 = BaseModel()

        # Test if the new object "Base1" is inserted into the "__objects" dict
        # Check if the object is inserted with the key: <object class name>.id
        self.assertIn(f"{Base1.__class__.__name__}.{Base1.id}",
                      storage._FileStorage__objects)

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
            f_dict = json.load(fp)
            self.assertTrue(f"{Base2.__class__.__name__}.{Base2.id}" in f_dict)
            self.assertTrue(f"{Base3.__class__.__name__}.{Base3.id}" in f_dict)
            self.assertTrue(f"{Base4.__class__.__name__}.{Base4.id}" in f_dict)

        # Test if the ids of the saved objects are same as original objects
            self.assertEqual(f_dict[f"{Base2.__class__.__name__}"
                             f".{Base2.id}"]["id"], Base2.id)
            self.assertEqual(f_dict[f"{Base3.__class__.__name__}"
                             f".{Base3.id}"]["id"], Base3.id)
            self.assertEqual(f_dict[f"{Base4.__class__.__name__}"
                             f".{Base4.id}"]["id"], Base4.id)

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
            self.assertIn(f"{Base5.__class__.__name__}.{Base5.id}",
                          FileStorage.__objects)
            self.assertIn(f"{Base6.__class__.__name__}.{Base6.id}",
                          FileStorage.__objects)
            self.assertIn(f"{Base7.__class__.__name__}.{Base7.id}",
                          FileStorage.__objects)

    def test_save_user(self):
        """Test if instance of User is correctly serialized & saved to file"""
        # Create and save to file instances of the User class
        user1 = User()
        user2 = User()
        user3 = User()
        user1.save()
        user2.save()
        user3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{user1.__class__.__name__}.{user1.id}", storage.all())
        self.assertIn(f"{user2.__class__.__name__}.{user2.id}", storage.all())
        self.assertIn(f"{user3.__class__.__name__}.{user3.id}", storage.all())

    def test_save_state(self):
        """Test if instance of State is correctly serialized & saved to file"""
        # Create and save to file instances of the State class
        state1 = State()
        state2 = State()
        state3 = State()
        state1.save()
        state2.save()
        state3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{state1.__class__.__name__}.{state1.id}",
                      storage.all())
        self.assertIn(f"{state2.__class__.__name__}.{state2.id}",
                      storage.all())
        self.assertIn(f"{state3.__class__.__name__}.{state3.id}",
                      storage.all())

    def test_save_city(self):
        """Test if instance of City is correctly serialized & saved to file"""
        # Create and save to file instances of the City class
        city1 = City()
        city2 = City()
        city3 = City()
        city1.save()
        city2.save()
        city3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{city1.__class__.__name__}.{city1.id}", storage.all())
        self.assertIn(f"{city2.__class__.__name__}.{city2.id}", storage.all())
        self.assertIn(f"{city3.__class__.__name__}.{city3.id}", storage.all())

    def test_save_amenity(self):
        """Test if instance of Amenity is correctly serialized/saved to file"""
        # Create and save to file instances of the Amenity class
        amenity1 = Amenity()
        amenity2 = Amenity()
        amenity3 = Amenity()
        amenity1.save()
        amenity2.save()
        amenity3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{amenity1.__class__.__name__}.{amenity1.id}",
                      storage.all())
        self.assertIn(f"{amenity2.__class__.__name__}.{amenity2.id}",
                      storage.all())
        self.assertIn(f"{amenity3.__class__.__name__}.{amenity3.id}",
                      storage.all())

    def test_save_place(self):
        """Test if instance of Place is correctly serialized & saved to file"""
        # Create and save to file instances of the Place class
        place1 = Place()
        place2 = Place()
        place3 = Place()
        place1.save()
        place2.save()
        place3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{place1.__class__.__name__}.{place1.id}",
                      storage.all())
        self.assertIn(f"{place2.__class__.__name__}.{place2.id}",
                      storage.all())
        self.assertIn(f"{place3.__class__.__name__}.{place3.id}",
                      storage.all())

    def test_save_review(self):
        """Test if instance of Review is correctly serialized/saved to file"""
        # Create and save to file instances of the Review class
        review1 = Review()
        review2 = Review()
        review3 = Review()
        review1.save()
        review2.save()
        review3.save()

        # Test if the instances are saved to file and reloaded correctly
        from models.__init__ import storage
        storage.reload()
        self.assertIn(f"{review1.__class__.__name__}.{review1.id}",
                      storage.all())
        self.assertIn(f"{review2.__class__.__name__}.{review2.id}",
                      storage.all())
        self.assertIn(f"{review3.__class__.__name__}.{review3.id}",
                      storage.all())
