#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""
This is the test_base_model to test base_model module.
This is a TestBaseModel class inside the test_base_model module.
"""


class TestBaseModel(unittest.TestCase):
    """This is a TestBaseModel class"""

    def setUp(self):
        """create the object base_model"""
        self.base_model = BaseModel()

    def test___init__(self):
        """method to check if instance initializes"""
        self.assertIsNotNone(self.base_model)

    def test_nones(self):
        """Test if id, created_at, updated_at has a value."""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_attributes(self):
        """method to test if basemodel has attributes id, created_at,
        updated_at
        """
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertTrue(hasattr(self.base_model, "id"))

    def test_types(self):
        """method to test if basemodel has attributes id, created_at,
        updated_at
        """
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_unique_id(self):
        """Test if ids are unique."""
        base_model_2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model_2.id)

    def tearDown(self):
        """dispose the object base_model"""
        self.base_model = None


if __name__ == "__main__":
    main()
