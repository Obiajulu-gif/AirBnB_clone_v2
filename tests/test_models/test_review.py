#!/usr/bin/python3
"""Unittest for review.py
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8

class TestReview(unittest.TestCase):
    """Test the Review class
    """
    def test_pep8_conformance(self):
        """Test that models/review.py conforms to PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test for docstrings
        """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Test the attributes of Review class
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel
        """
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel), True)

    def test_save(self):
        """Test the save method
        """
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")

    def test_str(self):
        """Test the __str__ method
        """
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
