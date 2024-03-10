#!/usr/bin/env python3
"""
    Test module for the class User of the Airbnb app
"""
from models.__init__ import storage
from models.user import User


class TestUser(unittest.TestCase):
    """Test class for the class User that inherits from BaseModel"""
    def test_attr(self):
        """Test for the public class attributes.

        Attributes: email, password, first_name and last_name
        """
        # Test if the public attributes exist
        self.assertTrue(hasattr(User, "email"))
        self.assertrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

        # Test if the public attributes are of type string
        self.asserttrue(type(User.email).__name__, "str")
        self.asserttrue(type(User.password).__name__, "str")
        self.asserttrue(type(User.first_name).__name__, "str")
        self.asserttrue(type(User.last_name).__name__, "str")

        # Create and save to file an instance of the class User
        user1 = User()
        user1.save()

        # check if instance has the same class attributes
        self.assertTrue(hasattr(user1, "email"))
        self.assertrue(hasattr(user1, "password"))
        self.assertTrue(hasattr(user1, "first_name"))
        self.assertTrue(hasattr(user1, "last_name"))

        # Test if instance of User is saved to file
        self.assertIn(f"{user1.__class__.__name__}.{user1.id}", storage.all())
        storage.reload()
        self.assertIn(f"{user1.__class__.__name__}.{user1.id}", storage.all())


        # Create additional instances of User and save to file
        user2 = User()
        user3 = User()
        user3 = User()
        user2.save()
        user3.save()
        user4.save()

        # Test if additional instances of User are saved to file
        storage.reload()
        self.assertIn(f"{user2.__class__.__name__}.{user2.id}", storage.all())
        self.assertIn(f"{user3.__class__.__name__}.{user3.id}", storage.all())
        self.assertIn(f"{user4.__class__.__name__}.{user4.id}", storage.all())
