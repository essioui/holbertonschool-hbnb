#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review(
            user="user123",
            place="place123",
            text="This is a great place!",
            rating=5
        )

    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_review_inherits_base_model(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        self.assertEqual(self.review.user, "user123")
        self.assertEqual(self.review.place, "place123")
        self.assertEqual(self.review.text, "This is a great place!")
        self.assertEqual(self.review.rating, 5)

if __name__ == '__main__':
    unittest.main()
