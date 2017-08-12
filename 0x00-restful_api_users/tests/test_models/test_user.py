#!/usr/bin/python3
import unittest
from models.user import User
"""
This is the test_user to test user module.
This is a TestUser class insemaile the test_user module.
"""


class TestUser(unittest.TestCase):
    """This is a TestUser class"""

    def setUp(self):
        """create the object user"""
        self.user = User()

    def test___init__(self):
        """method to check if instance initializes"""
        self.assertIsNotNone(self.user)

    def test_values(self):
        """Test if email, first_name, last_name has a value or not."""
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)
        self.user.email = "rose@gmail.com"
        self.assertIsNotNone(self.user.email)
        self.user.first_name = "rose"
        self.assertIsNotNone(self.user.first_name)
        self.user.last_name = "sinha"
        self.assertIsNotNone(self.user.last_name)

    def test_nones(self):
        """Test if id, created_at, updated_at has a value."""
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_attributes(self):
        """Test if User has attributes id, created_at, updated_at,
        email, first_name, last_name, password"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "_password"))

    def test_display_name(self):
        """Test if display_name works properly"""
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

    def test__str__(self):
        """Test __str__ method"""
        self.user.email = "hbtn@holbertonschool.com"
        self.assertNotEqual(str(self.user), "")
        op = "[{}] {} - {} - {}".format("User",
                                        self.user.id, self.user.email,
                                        self.user.display_name())
        self.assertEqual(str(self.user), op)

    def test_password(self):
        """Test password"""
        self.user.password = "hello"
        md5_password = "5d41402abc4b2a76b9719d911017c592"
        self.assertIsNotNone(self.user.password)
        # self.assertNotEqual(self.user.password, "hello")
        # self.assertEqual(self.user.password, md5_password)

    def tearDown(self):
        """dispose the object user"""
        self.user = None


if __name__ == "__main__":
    main()
