#!/usr/bin/python3
"""Unittest for amenity.py file
"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test the Amenity class
    """
    def test_pep8_conformance(self):
        """Test that models/amenity.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Test the attributes of Amenity class
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_str(self):
        """Test the __str__ method
        """
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))