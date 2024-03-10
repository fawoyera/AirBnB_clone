#!/usr/bin/env python3
"""
    Test module for the class State which inherits from BaseModel
"""
from models.__init__ import storage
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test class for the State class"""
    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """Test the public class attribute name"""
        # Test if the attribute name exist for class State
        self.assertTrue(hasattr(State, "name"))

        # Test if the type of attribute name is string
        self.assertTrue(type(State.name).__name__, "str"))

    def test_instance(self):
        """Test if instances are saved to file and reloaded correctly"""
        # Create and save to file instances of class State
        state1 = State()
        state2 = State()
        state3 = State()
        state1.save()
        state2.save()
        state3.save()

        # reload objects from file and test if instances are correctly loaded
        storage.reload()
        self.assertIn(f"{state1.__class__.__name__}.{state1.id}", storage.all())
        self.assertIn(f"{state2.__class__.__name__}.{state2.id}", storage.all())
        self.assertIn(f"{state3.__class__.__name__}.{state3.id}", storage.all())
