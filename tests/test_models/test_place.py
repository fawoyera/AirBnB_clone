#!/usr/bin/env python3
"""
    Test module for the class Place which inherits from BaseModel
"""
from models.__init__ import storage
from models.base_model import BaseModel
from models.place import Place


class TestState(unittest.TestCase):
    """Test class for the Place class"""
    def test_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """Test the public class attributes"""
        # Test if the attributes exist for class Place
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

        # Test if the type of attributes are correct
        self.assertTrue(type(Place.city_id).__name__, "str"))
        self.assertTrue(type(Place.user_id).__name__, "str"))
        self.assertTrue(type(Place.name).__name__, "str"))
        self.assertTrue(type(Place.description).__name__, "str"))
        self.assertTrue(type(Place.number_rooms).__name__, "int"))
        self.assertTrue(type(Place.number_bathrooms).__name__, "int"))
        self.assertTrue(type(Place.max_guest).__name__, "int"))
        self.assertTrue(type(Place.price_by_night).__name__, "int"))
        self.assertTrue(type(Place.latitude).__name__, "float"))
        self.assertTrue(type(Place.longitude).__name__, "float"))
        self.assertTrue(type(Place.amenity_ids).__name__, "list"))

    def test_instance(self):
        """Test if instance of Place is saved to file and reloaded"""
        # Create and save to file instances of class Place
        place1 = Place()
        place2 = Place()
        place3 = Place()
        place1.save()
        place2.save()
        place3.save()

        # reload object from file and test if instances are reloaded rightly
        storage.reload()
        self.assertIn(f"{place1.__class__.__name__}.{place1.id}", storage.all())
        self.assertIn(f"{place2.__class__.__name__}.{place2.id}", storage.all())
        self.assertIn(f"{place3.__class__.__name__}.{place3.id}", storage.all())
