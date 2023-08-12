#!/usr/bin/python3

""" This is used in testing the review class with method as follows:

    Testing_init_review
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class Testing_init_review(unittest.TestCase):
    """ This class tests the initialization method of review """

    def testing_init_review(self):
        """ testing init review """

        self.assertIsInstance(Review(), Review)

    def testing_init_subclass(self):
        """ testing init subclass """

        self.assertTrue(issubclass(Review, BaseModel))

    def testing_place_attribute(self):
        """ testing place attribute """

        new_review = Review()
        self.assertIsInstance(new_review.place_id, str)
        self.assertIn('place_id', dir(new_review))

    def testing_user_attribute(self):
        """ testing user attribute """

        new_review = Review()
        self.assertIsInstance(new_review.user_id, str)
        self.assertIn('user_id', dir(new_review))

    def testing_text_attribute(self):
        """ testing text attribute """

        new_review = Review()
        self.assertIsInstance(new_review.text, str)
        self.assertIn('text', dir(new_review))

    def testing_update(self):
        """ testing update """

        self.assertIsInstance(Review().updated_at, datetime)

    def testing_create(self):
        """ testing create """

        self.assertIsInstance(Review().created_at, datetime)

    def testing_with_kwargs(self):
        """ testing with kwargs """

        new_review = Review()
        new_dict = new_review.to_dict()
        Nview = Review(**new_dict)
        self.assertEqual(new_review.id, Nview.id)
        self.assertEqual(new_review.created_at, Nview.created_at)
        self.assertEqual(new_review.updated_at, Nview.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of review """

    def testing_save(self):
        """testing save """

        new_review = Review()
        new_update = new_review.updated_at
        new_review.save()
        self.assertLess(new_update, new_review.updated_at)

    def testing_save_file(self):
        """ testing save file """

        new_review = Review()
        new_review.save()
        new_review_id = 'Review.' + new_review.id
        with open('objects.json', 'r') as document:
            self.assertIn(new_review_id, document.read())

    def testing_with_arg(self):
        """ testing with arg """

        with self.assertRaises(TypeError):
            Review().save("please update class")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of review """

    def testing_dict(self):
        """ testing dict"""

        self.assertIsInstance(Review().to_dict(), dict)

    def testing_with_args(self):
        """ testing witgh args """

        with self.assertRaises(TypeError):
            Review().to_dict([])

    def testing_attribute(self):
        """testing attribute """

        new_review = Review()
        new_review.name = "review name"
        self.assertIn('name', new_review.to_dict())

    def testing_dict_keys(self):
        """testing dict keys """

        new_review = Review()
        self.assertIn('id', new_review.to_dict())
        self.assertIn('created_at', new_review.to_dict())
        self.assertIn('updated_at', new_review.to_dict())

    def testing_dict_values(self):
        """ testing dict values """

        new_review = Review()
        new_dict = new_review.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
