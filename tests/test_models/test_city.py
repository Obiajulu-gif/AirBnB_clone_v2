#!/usr/bin/python3
"""Unittest for city.py
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8

class TestCity(unittest.TestCase):
    """Test the City class
    """
    def test_pep8_conformance(self):
        """Test that models/city.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test the attributes of City class
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel
        """
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")

    def test_str(self):
        """Test the __str__ method
        """
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
    