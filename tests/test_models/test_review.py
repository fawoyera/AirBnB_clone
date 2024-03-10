#!/usr/bin/env python3
"""
    Test module for the class Review which inherits from BaseModel
"""
from models.__init__ import storage
from models.base_model import BaseModel
from models.review import Review


class TestState(unittest.TestCase):
    """Test class for the Review class"""
    def test_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr(self):
        """Test the public class attributes of class Review"""
        # Test if the attributes exist for class review
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

        # Test if the type of attributes is string
        self.assertTrue(type(Review.place_id).__name__, "str"))
        self.assertTrue(type(Review.user_id).__name__, "str"))
        self.assertTrue(type(Review.text).__name__, "str"))

    def test_instance(self):
        """Test if instances are saved to file and reloaded correctly"""
        # Create and save to file instances of class Review
        review1 = Review()
        review2 = Review()
        review3 = Review()
        review1.save()
        review2.save()
        review3.save()

        # reload objects from file and test if instances are correctly loaded
        storage.reload()
        self.assertIn(f"{review1.__class__.__name__}.{review1.id}", storage.all())
        self.assertIn(f"{review2.__class__.__name__}.{review2.id}", storage.all())
        self.assertIn(f"{review3.__class__.__name__}.{review3.id}", storage.all())
