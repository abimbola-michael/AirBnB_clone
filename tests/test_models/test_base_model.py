#!/usr/bin/python3
""" This takes the BaseModel class and tests each unit as follows:
Testing_init, Testing_kwargs, Testing_str
Testing_save, Testing_dict
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class Testing_init(unittest.TestCase):
    """ This tests for the init method in the BaseModel. """

    def testing_BaseModel_as_obj(self):
        """testing basemodel as an object """

        self.assertIsInstance(BaseModel(), BaseModel)

    def testing_uniqueness(self):
        """ testing uniqueness"""

        opt1 = BaseModel()
        opt2 = BaseModel()
        opt3 = BaseModel()
        opt4 = BaseModel()
        self.assertNotEqual(opt1.id, opt2.id)
        self.assertNotEqual(opt1.id, opt3.id)
        self.assertNotEqual(opt1.id, opt4.id)
        self.assertNotEqual(opt2.id, opt3.id)
        self.assertNotEqual(opt2.id, opt4.id)
        self.assertNotEqual(opt3.id, opt4.id)

    def testing_for_args(self):
        """ testing for args """

        self.assertIsInstance(BaseModel(), BaseModel)

    def testing_for_id(self):
        """ testing for id """

        opt1 = BaseModel()
        opt2 = BaseModel()
        self.assertEqual(type(BaseModel().id), str)
        self.assertEqual(type(opt1.id), type(opt2.id))

    def testing_update_uniqueness(self):
        """ testing update uniqueness """

        opt1 = BaseModel()
        opt2 = BaseModel()
        self.assertNotEqual(opt1.updated_at, opt2.updated_at)

    def testing_update_type(self):
        """ testing basemodel update type """

        opt1 = BaseModel()
        opt2 = BaseModel()
        self.assertIsInstance(BaseModel().updated_at, datetime)
        self.assertEqual(type(opt1.updated_at), type(opt2.updated_at))

    def testing_create_type(self):
        """ testing basemodel create type """

        opt1 = BaseModel()
        opt2 = BaseModel()
        self.assertIsInstance(opt1.created_at, datetime)
        self.assertEqual(type(opt1.created_at), type(opt2.created_at))

    def testing_create_uniqueness(self):
        """ testing basemodel uniqueness """

        opt1 = BaseModel()
        opt2 = BaseModel()
        self.assertNotEqual(opt1.created_at, opt2.created_at)


class Testing_kwargs(unittest.TestCase):
    """ This tests the inti method putting the kwargs in view """

    def testing_basemodel_create(self):
        """testing and comparing basemodel create """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        self.assertEqual(str(new_base), str(test_base))
        fin_str = "[" + new_base.__class__.__name__ + \
            "] (" + new_base.id + ") " + str(new_base.__dict__)
        self.assertEqual(fin_str, str(new_base))

    def testing_basemodel_created(self):
        """ testing basemodel create """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        self.assertIsInstance(test_base.created_at, datetime)

    def testing_basemodel_update(self):
        """ testing basemodel update """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        self.assertIsInstance(test_base.updated_at, datetime)

    def testing_basemodels(self):
        """ testing basemodel """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        self.assertNotEqual(new_base, test_base)

    def testing_for_same_basemodel(self):
        """ testing for same basemodel """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        self.assertIsNot(new_base, test_base)

    def testing_basemodel_attributes(self):
        """ testing basemodel  attributes """

        new_base = BaseModel()
        new_dict = new_base.to_dict()
        test_base = BaseModel(**new_dict)
        with self.assertRaises(KeyError):
            print(test_base.__dict__[__class__])


class Testing_str(unittest.TestCase):
    """ Testing the string method in the basemodel"""

    def testing_str(self):
        """ testing string """

        new_str = BaseModel().__str__()
        self.assertIsInstance(new_str, str)

    def testing_format(self):
        """ testing format """

        new_base = BaseModel()
        new_class = new_base.__class__
        new_id = new_base.id
        fin_str = "[" + new_base.__class__.__name__ + \
            "] (" + new_base.id + ") " + str(new_base.__dict__)
        self.assertEqual(new_base.__str__(), fin_str)


class Testing_save(unittest.TestCase):
    """ testing the save method in the basemodel"""

    def testing_save(self):
        """ testing save """

        new_base = BaseModel()
        new_base.save()
        self.assertIsInstance(new_base.updated_at, datetime)

    def testing_save_value(self):
        """ testing saved value """

        new_base = BaseModel()
        prv_update = new_base.updated_at
        new_base.save()
        self.assertNotEqual(new_base.updated_at, prv_update)

    def testing_save_with_arg(self):
        """ testing save with arg """

        with self.assertRaises(TypeError):
            BaseModel().save(datetime.now())
        with self.assertRaises(TypeError):
            BaseModel().save({"key": "value"})
        with self.assertRaises(TypeError):
            BaseModel().save(863, "two_args")

    def testing_save_without_arg(self):
        """ testing sace without argument """

        new_base = BaseModel()
        prv_update = new_base.updated_at
        new_base.save()
        self.assertNotEqual(new_base.updated_at, prv_update)


class Testing_dict(unittest.TestCase):
    """ this is to test the dict of the basemodel """

    def testing_updated_dict(self):
        """ testing updated dict """

        new_base = BaseModel()
        new_update = new_base.to_dict().get('updated_at', None)
        self.assertIsInstance(new_update, str)

    def testing_created_dict(self):
        """ testing created dict """

        new_base = BaseModel().to_dict()
        new_create = new_base.get('created_at', None)
        self.assertIsInstance(new_create, str)

    def testing_dict_value(self):
        """ testing dict value """

        self.assertIsInstance(BaseModel().to_dict(), dict)

    def testing_with_arg(self):
        """ testing wit arg """

        with self.assertRaises(TypeError):
            BaseModel().to_dict("one arg")

        with self.assertRaises(TypeError):
            BaseModel().to_dict(9, 87)

        with self.assertRaises(TypeError):
            BaseModel().to_dict(
                "first arg", ["a list"], ("a tuple", "with another element"))

    def testing_without_arg(self):
        """ testing without arg """

        self.assertIsInstance(BaseModel().to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
