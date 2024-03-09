#!/usr/bin/env python3
"""
    Test module for Base Model of the AirBnB Clone
"""
import datetime
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
        Test Class for BaseModel
    """
    def test_init(self):
        """ Test the initialization of instance attributes
        """
        b0 = BaseModel()
        self.assertIsInstance(b0, BaseModel)
        self.assertTrue(hasattr(b0, "id"))
        self.assertTrue(hasattr(b0, "created_at"))
        self.assertTrue(hasattr(b0, "updated_at"))
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertEqual(type(b1.id).__name__, "str")  # id is string
        self.assertEqual(type(b1.created_at).__name__, "datetime")
        self.assertEqual(type(b1.updated_at).__name__, "datetime")
        self.assertNotEqual(b1.id, b2.id)  # unique ids
        self.assertTrue(b2.created_at > b1.created_at)
        self.assertTrue(b1.updated_at >= b1.created_at)
        self.assertTrue(b2.updated_at >= b2.created_at)

    def test_init_args(self):
        """ Test the initialization of instance attributes with keyword args
        """
        b7 = BaseModel()
        b7_dict = b7.to_dict()
        b8 = BaseModel(**b7_dict)
        self.assertEqual(b8.id, b7.id)
        self.assertEqual(b8.created_at, b7.created_at)
        self.assertEqual(b8.updated_at, b7.updated_at)

    def test__str__(self):
        """ Test the __str__ method
        """
        b3 = BaseModel()
        self.assertEqual(print(b3), None)

    def test_save(self):
        """ Test the public instance method save
        """
        b4 = BaseModel()
        old_date = b4.updated_at
        b4.save()
        new_date = b4.updated_at
        self.assertGreater(new_date, old_date)

    def test_to_dict(self):
        """ Test the public instance method to_dict
        """
        b5 = BaseModel()
        try:
            b5.created_at = datetime.datetime(2024, 3, 6, 13, 16, 36, 890872)
            b5.updated_at = datetime.datetime(2024, 3, 6, 13, 26, 36, 890874)
        except Exception:
            pass
        else:
            self.assertEqual(b5.to_dict(), {"id": b5.id,
                                            "created_at":
                                            "2024-03-06T13:16:36.890872",
                                            "updated_at":
                                            "2024-03-06T13:26:36.890874",
                                            "__class__":
                                            b5.__class__.__name__})
        b6 = BaseModel()
        self.assertEqual(b6.to_dict(), {"id": b6.id,
                                        "created_at":
                                        b6.created_at.isoformat(),
                                        "updated_at":
                                        b6.updated_at.isoformat(),
                                        "__class__":
                                        b6.__class__.__name__})

    def test_storage(self):
        """ Test if BaseModel instance is stored in the FileStorage on init
        """
        # Initialize FileStorage
        storage = FileStorage()
        storage.relaod()

        # Create a BaseModel instance
        b1 = BaseModel()

        # Check if object is stored in memory and file after save
        self.assertIn(f"{b1.__class__.__name__}.{b1.id}", storage.all())
        b1.save()
        self.assertIn(f"{b1.__class__.__name__}.{b1.id}", storage.all())

        # Create additional BaseModel instances
        b2 = BaseModel()
        b3 = BaseModel()

        # Save additional instances & check if they are stored in memory/file
        b2.save()
        b3.save()
        self.assertIn(f"{b2.__class__.__name__}.{b2.id}", storage.all())
        self.assertIn(f"{b3.__class__.__name__}.{b3.id}", storage.all())

        # Reload FileStorage from file
        storage.relaod()

        # Check if objects are correctly loaded from file upon reload
        self.assertIn(f"{b1.__class__.__name__}.{b1.id}", storage.all())
        self.assertIn(f"{b2.__class__.__name__}.{b2.id}", storage.all())
        self.assertIn(f"{b3.__class__.__name__}.{b3.id}", storage.all())
