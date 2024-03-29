#!/usr/bin/python3

""" This is used in testing the city class with method as follows:

    Testing_init_city
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class Testing_init_city(unittest.TestCase):
    """ This class tests the initialization method of city """

    def testing_init_city(self):
        """ testing init city """

        self.assertIsInstance(City(), City)

    def testing_init_subclass(self):
        """testing init subclass """

        self.assertTrue(issubclass(City, BaseModel))

    def testing_nameattribute(self):
        """ testing name attribute """

        new_city = City()
        self.assertIsInstance(new_city.name, str)
        self.assertIn('name', dir(new_city))

    def testing_idattribute(self):
        """ testing id attribute """

        new_city = City()
        self.assertIsInstance(new_city.state_id, str)
        self.assertIn('state_id', dir(new_city))

    def testing_update(self):
        """ testing update """

        self.assertIsInstance(City().updated_at, datetime)

    def testing_create(self):
        """testing create """

        self.assertIsInstance(City().created_at, datetime)

    def testing_with_kwargs(self):
        """ testing with dict """

        new_city = City()
        new_dict = new_city.to_dict()
        Ncity = City(**new_dict)
        self.assertEqual(new_city.id, Ncity.id)
        self.assertEqual(new_city.created_at, Ncity.created_at)
        self.assertEqual(new_city.updated_at, Ncity.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of city """

    def testing_save(self):
        """ testing save """

        new_city = City()
        new_update = new_city.updated_at
        new_city.save()
        self.assertLess(new_update, new_city.updated_at)

    def testing_save_file(self):
        """testing save file """

        new_city = City()
        new_city.save()
        new_city_id = 'City.' + new_city.id
        with open('file.json', 'r') as document:
            self.assertIn(new_city_id, document.read())

    def testing_with_arg(self):
        """ testing with dict """

        with self.assertRaises(TypeError):
            City().save("Save Now")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of city """

    def testing_dict(self):
        """ testing dict """

        self.assertIsInstance(City().to_dict(), dict)

    def testing_with_args(self):
        """ testing with args """

        with self.assertRaises(TypeError):
            City().to_dict(555)

    def testing_attribute(self):
        """ testing attribute """

        new_city = City()
        new_city.name = "My name"
        self.assertIn('name', new_city.to_dict())

    def testing_dict_keys(self):
        """ testing dict keys """

        new_city = City()
        self.assertIn('id', new_city.to_dict())
        self.assertIn('created_at', new_city.to_dict())
        self.assertIn('updated_at', new_city.to_dict())
        self.assertIn('__class__', new_city.to_dict())

    def testing_dict_values(self):
        """ testing dict values """

        new_city = City()
        new_dict = new_city.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
