#!/usr/bin/python3

""" This is used in testing the user class with method as follows:

    Testing_init_user
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class Testing_init_user(unittest.TestCase):
    """ This class tests the initialization method of user """

    def testing_init_user(self):
        self.assertIsInstance(User(), User)

    def testing_init_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))

    def testing_email_attribute(self):
        new_user = User()
        self.assertIsInstance(new_user.email, str)
        self.assertIn('email', dir(new_user))

    def testing_password_attribute(self):
        new_user = User()
        self.assertIsInstance(new_user.password, str)
        self.assertIn('password', dir(new_user))

    def testing_first_name_attribute(self):
        new_user = User()
        self.assertIsInstance(new_user.first_name, str)
        self.assertIn('first_name', dir(new_user))

    def testing_last_name_attribute(self):
        new_user = User()
        self.assertIsInstance(new_user.last_name, str)
        self.assertIn('last_name', dir(new_user))

    def testing_update(self):
        self.assertIsInstance(User().updated_at, datetime)

    def testing_create(self):
        self.assertIsInstance(User().created_at, datetime)

    def testing_with_kwargs(self):
        new_user = User()
        new_dict = new_user.to_dict()
        Nuser = User(**new_dict)
        self.assertEqual(new_user.id, Nuser.id)
        self.assertEqual(new_user.created_at, Nuser.created_at)
        self.assertEqual(new_user.updated_at, Nuser.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of user """

    def testing_save(self):
        new_user = User()
        new_update = new_user.updated_at
        new_user.save()
        self.assertLess(new_update, new_user.updated_at)

    def testing_save_file(self):
        new_user = User()
        new_user.save()
        new_user_id = 'User.' + new_user.id
        with open('objects.json', 'r') as document:
            self.assertIn(new_user_id, document.read())

    def testing_with_arg(self):
        with self.assertRaises(TypeError):
            User().save("please update the class")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of User """

    def testing_dict(self):
        self.assertIsInstance(User().to_dict(), dict)

    def testing_with_args(self):
        with self.assertRaises(TypeError):
            User().to_dict([])

    def testing_attribute(self):
        new_user = User()
        new_user.name = "User name"
        self.assertIn('name', new_user.to_dict())

    def testing_dict_keys(self):
        new_user = User()
        self.assertIn('id', new_user.to_dict())
        self.assertIn('created_at', new_user.to_dict())
        self.assertIn('updated_at', new_user.to_dict())

    def testing_dict_values(self):
        new_user = User()
        new_dict = new_user.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
