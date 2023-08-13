#!/usr/bin/python3

""" This is used in testing the amenity class with method as follows:

    Testing_init_amenity
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class Testing_init_amenity(unittest.TestCase):
    """ This class tests the initialization class of amenity """

    def testing_init_amenity(self):
        """ testing initialization"""

        self.assertIsInstance(Amenity(), Amenity)

    def testing_init_subclass(self):
        """ testing initialization of subclass """

        self.assertTrue(issubclass(Amenity, BaseModel))

    def testing_attribute(self):
        """ testing attribute """

        new_amen = Amenity()
        self.assertIsInstance(new_amen.name, str)
        self.assertIn('name', dir(new_amen))

    def testing_update(self):
        """ testing update """

        self.assertIsInstance(Amenity().updated_at, datetime)

    def testing_create(self):
        """ testing create """

        self.assertIsInstance(Amenity().created_at, datetime)

    def testing_with_kwargs(self):
        """ testing with dict """

        new_amen = Amenity()
        new_dict = new_amen.to_dict()
        amen = Amenity(**new_dict)
        self.assertEqual(new_amen.id, amen.id)
        self.assertEqual(new_amen.created_at, amen.created_at)
        self.assertEqual(new_amen.updated_at, amen.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of amenity """

    def testing_save(self):
        """ testing save """

        new_amen = Amenity()
        new_update = new_amen.updated_at
        new_amen.save()
        self.assertLess(new_update, new_amen.updated_at)

    def testing_save_file(self):
        """ testing saved files """

        new_amen = Amenity()
        new_amen.save()
        new_amen_id = 'Amenity.' + new_amen.id
        with open('file.json', 'r') as document:
            self.assertIn(new_amen_id, document.read())

    def testing_with_arg(self):
        """ testing with args """

        with self.assertRaises(TypeError):
            Amenity().save("update the class")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of amenity """

    def testing_dict(self):
        """ testing dictionary """

        self.assertIsInstance(Amenity().to_dict(), dict)

    def testing_with_args(self):
        """ testing dict with arg """

        with self.assertRaises(TypeError):
            Amenity().to_dict([])

    def testing_attribute(self):
        """ testing attribute """

        new_amen = Amenity()
        new_amen.name = "Amenity name"
        self.assertIn('name', new_amen.to_dict())

    def testing_dict_keys(self):
        """ testing dict keys """

        new_amen = Amenity()
        self.assertIn('id', new_amen.to_dict())
        self.assertIn('created_at', new_amen.to_dict())
        self.assertIn('updated_at', new_amen.to_dict())

    def testing_dict_values(self):
        """ testing dictionary value"""

        new_amen = Amenity()
        new_dict = new_amen.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
