#!/usr/bin/env python3
"""
    Test module for the class City which inherits from BaseModel
"""
from models.__init__ import storage
from models.base_model import BaseModel
from models.city import City
import unittest


class TestState(unittest.TestCase):
    """Test class for the City class"""
    def test_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr(self):
        """Test the public class attribute state_id and name"""
        # Test if the attribute state_id and name exist for class City
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

        # Test if the type of attributes state_id and name is string
        self.assertTrue(type(City.state_id).__name__, "str")
        self.assertTrue(type(City.name).__name__, "str")

    def test_instance(self):
        """Test if instance of City is saved to file and reloaded"""
        # Create and save to file instances of class City
        city1 = City()
        city2 = City()
        city3 = City()
        city1.save()
        city2.save()
        city3.save()

        # reload object from file and test if instances are reloaded rightly
        storage.reload()
        self.assertIn(f"{city1.__class__.__name__}.{city1.id}", storage.all())
        self.assertIn(f"{city2.__class__.__name__}.{city2.id}", storage.all())
        self.assertIn(f"{city3.__class__.__name__}.{city3.id}", storage.all())
