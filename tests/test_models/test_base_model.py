#!/usr/bin/python3
"""Unittest for base_model.py
"""

import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class
    """
    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_attributes(self):
        """Test the attributes of BaseModel class
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))

    def test_is_subclass(self):
        """Test if BaseModel is a subclass of BaseModel
        """
        base_model = BaseModel()
        self.assertTrue(issubclass(base_model.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")

    def test_str(self):
        """Test the __str__ method
        """
        base_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(base_model.id,
                                              base_model.__dict__)
        self.assertEqual(string, str(base_model))
