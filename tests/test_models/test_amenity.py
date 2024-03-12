#!/usr/bin/env python3
"""
    Test module for the class Amenity which inherits from BaseModel
"""
from models.__init__ import storage
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestState(unittest.TestCase):
    """Test class for the Amenity class"""
    def test_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """Test the public class attribute  name"""
        # Test if the attribute name exist for class Amenity
        self.assertTrue(hasattr(Amenity, "name"))

        # Test if the type of attributes name is string
        self.assertTrue(type(Amenity.name).__name__, "str")

    def test_instance(self):
        """Test if instance of Amenity is saved to file and reloaded"""
        # Create and save to file instances of class Amenity
        amenity1 = Amenity()
        amenity2 = Amenity()
        amenity3 = Amenity()
        amenity1.save()
        amenity2.save()
        amenity3.save()

        # reload object from file and test if instances are reloaded rightly
        storage.reload()
        self.assertIn(f"{amenity1.__class__.__name__}.{amenity1.id}",
                      storage.all())
        self.assertIn(f"{amenity2.__class__.__name__}.{amenity2.id}",
                      storage.all())
        self.assertIn(f"{amenity3.__class__.__name__}.{amenity3.id}",
                      storage.all())
