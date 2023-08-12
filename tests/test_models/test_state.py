#!/usr/bin/python3

""" This is used in testing the state class with method as follows:

    Testing_init_state
    Testing_save
    Testing_to_dict
"""


import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class Testing_init_state(unittest.TestCase):
    """ This class tests the initialization method of state """

    def testing_init_state(self):
        """ testing state init """

        self.assertIsInstance(State(), State)

    def testing_init_subclass(self):
        """ testing state subclass"""

        self.assertTrue(issubclass(State, BaseModel))

    def testing_nameattribute(self):
        """ testing nsme attribute """

        new_state = State()
        self.assertIsInstance(new_state.name, str)
        self.assertIn('name', dir(new_state))

    def testing_update(self):
        """ testing update """

        self.assertIsInstance(State().updated_at, datetime)

    def testing_create(self):
        """ testing create """

        self.assertIsInstance(State().created_at, datetime)

    def testing_with_kwargs(self):
        """ testing with kwargs """

        new_state = State()
        new_dict = new_state.to_dict()
        Nstate = State(**new_dict)
        self.assertEqual(new_state.id, Nstate.id)
        self.assertEqual(new_state.created_at, Nstate.created_at)
        self.assertEqual(new_state.updated_at, Nstate.updated_at)


class Testing_save(unittest.TestCase):
    """ This class tests the method class of state """

    def testing_save(self):
        """ testing save """

        new_state = State()
        new_update = new_state.updated_at
        new_state.save()
        self.assertLess(new_update, new_state.updated_at)

    def testing_save_file(self):
        """ testing save file """

        new_state = State()
        new_state.save()
        new_state_id = 'State.' + new_state.id
        with open('objects.json', 'r') as document:
            self.assertIn(new_state_id, document.read())

    def testing_with_arg(self):
        """ testing with arg """

        with self.assertRaises(TypeError):
            State().save("please update the class")


class Testing_to_dict(unittest.TestCase):
    """ This class tests the dict method of state """

    def testing_dict(self):
        """ testing dict """

        self.assertIsInstance(State().to_dict(), dict)

    def testing_with_args(self):
        """ testing with args """

        with self.assertRaises(TypeError):
            State().to_dict([])

    def testing_attribute(self):
        """ testing attribute """

        new_state = State()
        new_state.name = "State name"
        self.assertIn('name', new_state.to_dict())

    def testing_dict_keys(self):
        """ testing dict keys """

        new_state = State()
        self.assertIn('id', new_state.to_dict())
        self.assertIn('created_at', new_state.to_dict())
        self.assertIn('updated_at', new_state.to_dict())

    def testing_dict_values(self):
        """ testing dict value """

        new_state = State()
        new_dict = new_state.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
