#!/usr/bin/python3
import unittest
from models.user import User
"""
This is the test_user to test user module.
This is a TestUser class insemaile the test_user module.
"""


class TestUser(unittest.TestCase):
    """
    This is a TestUser class
    """

    def setUp(self):
        """
        create the object user
        """
        self.user = User()

    def test___init__(self):
        """
        method to check if instance initializes
        """
        self.assertIsNotNone(self.user)

    def test_values(self):
        """
        Test if email, first_name, last_name has a value or not.
        """
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)
        self.user.email = "rose@gmail.com"
        self.assertIsNotNone(self.user.email)
        self.user.first_name = "rose"
        self.assertIsNotNone(self.user.first_name)
        self.user.last_name = "sinha"
        self.assertIsNotNone(self.user.last_name)

    def test_attributes(self):
        """
        method to test if User has attributes email, first_name, last_name
        """
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "email"))

    def test_display_name(self):
        """
        method to check if display_name works properly
        """
        self.assertEqual(self.user.display_name(), "")
        self.user.email = "rose@gmail.com"
        self.assertEqual(self.user.display_name(), "rose@gmail.com")
        self.assertNotEqual(self.user.display_name(), "rose sinha")
        self.user.first_name = "rose"
        self.assertEqual(self.user.display_name(), "rose")
        self.assertNotEqual(self.user.display_name(), "rose@gmail.com")
        self.user.last_name = "sinha"
        self.assertEqual(self.user.display_name(), "rose sinha")
        self.assertNotEqual(self.user.display_name(), "rose")

    def tearDown(self):
        """
        dispose the object user
        """
        self.user = None


if __name__ == "__main__":
    main()
