#!/usr/bin/python3

""" This is used in testing the place class with method as follows:

    Testing_init_place
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class Testing_init_city(unittest.TestCase):
    """ This class tests the initialization method of place """

    def testing_init_place(self):
        """ testing init """

        self.assertIsInstance(Place(), Place)

    def testing_init_subclass(self):
        """ testing subclass """

        self.assertTrue(issubclass(Place, BaseModel))

    def testing_nameattribute(self):
        """ testing name attribute """

        new_place = Place()
        self.assertIsInstance(new_place.name, str)
        self.assertIn('name', dir(new_place))

    def testing_city_attribute(self):
        """ testing city attribute """

        new_place = Place()
        self.assertIsInstance(new_place.city_id, str)
        self.assertIn('city_id', dir(new_place))

    def testing_user_attribute(self):
        """ testing user attribute """

        new_place = Place()
        self.assertIsInstance(new_place.user_id, str)
        self.assertIn('user_id', dir(new_place))

    def testing_description_attribute(self):
        """ testing description attribute """

        new_place = Place()
        self.assertIsInstance(new_place.description, str)
        self.assertIn('description', dir(new_place))

    def testing_number_rooms_attribute(self):
        """ testing number of rooms attribute """

        new_place = Place()
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIn('number_rooms', dir(new_place))

    def testing_number_bathrooms_attribute(self):
        """ testing number of bathrooms attribute """

        new_place = Place()
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIn('number_bathrooms', dir(new_place))

    def testing_max_guest_attribute(self):
        """testing max guest attribute """

        new_place = Place()
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIn('max_guest', dir(new_place))

    def testing_price_by_night_attribute(self):
        """ testing price by night attribute """

        new_place = Place()
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertIn('price_by_night', dir(new_place))

    def testing_latitude_attribute(self):
        """ testing latitude attribute """

        new_place = Place()
        self.assertIsInstance(new_place.latitude, float)
        self.assertIn('latitude', dir(new_place))

    def testing_longitude_attribute(self):
        """ testing longitude attribute """

        new_place = Place()
        self.assertIsInstance(new_place.longitude, float)
        self.assertIn('longitude', dir(new_place))

    def testing_amenity_ids_attribute(self):
        """ testing amenity ids attribute """

        new_place = Place()
        self.assertIsInstance(new_place.amenity_ids, list)
        self.assertIn('amenity_ids', dir(new_place))

    def testing_update(self):
        """ testing update """

        self.assertIsInstance(Place().updated_at, datetime)

    def testing_create(self):
        """ testing create """

        self.assertIsInstance(Place().created_at, datetime)

    def testing_with_kwargs(self):
        """ testing with dict """

        new_place = Place()
        new_dict = new_place.to_dict()
        Nplace = Place(**new_dict)
        self.assertEqual(new_place.id, Nplace.id)
        self.assertEqual(new_place.created_at, Nplace.created_at)
        self.assertEqual(new_place.updated_at, Nplace.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of place """

    def testing_save(self):
        """ testing save """

        new_place = Place()
        new_update = new_place.updated_at
        new_place.save()
        self.assertLess(new_update, new_place.updated_at)

    def testing_save_file(self):
        """ testing save file """

        new_place = Place()
        new_place.save()
        new_place_id = 'Place.' + new_place.id
        with open('file.json', 'r') as document:
            self.assertIn(new_place_id, document.read())

    def testing_with_arg(self):
        """ testing with arg """

        with self.assertRaises(TypeError):
            Place().save("please update the class")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of place """

    def testing_dict(self):
        """ testing dict """

        self.assertIsInstance(Place().to_dict(), dict)

    def testing_with_args(self):
        """ testing with args """

        with self.assertRaises(TypeError):
            Place().to_dict([])

    def testing_attribute(self):
        """ testing attribute """

        new_place = Place()
        new_place.name = "Place name"
        self.assertIn('name', new_place.to_dict())

    def testing_dict_keys(self):
        """ testing dict keys """

        new_place = Place()
        self.assertIn('id', new_place.to_dict())
        self.assertIn('created_at', new_place.to_dict())
        self.assertIn('updated_at', new_place.to_dict())

    def testing_dict_values(self):
        """ testing dict values """

        new_place = Place()
        new_dict = new_place.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
