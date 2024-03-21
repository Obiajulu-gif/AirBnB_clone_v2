#!/usr/bin/python3
"""Unittest for state.py
"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test the State class
    """
    def test_pep8_conformance(self):
        """Test that models/state.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Test the attributes of State class
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel
        """
        state = State()
        self.assertTrue(issubclass(state.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
