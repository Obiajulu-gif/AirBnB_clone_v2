#!/usr/bin/python3
"""Unittest for user.py
"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """Test the User class
    """
    def test_pep8_conformance(self):
        """Test that models/user.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Test the attributes of User class
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel
        """
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")

    def test_str(self):
        """Test the __str__ method
        """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
