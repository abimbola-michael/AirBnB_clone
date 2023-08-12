#!/usr/bin/python3

""" this tests class in the file storage class as follows:

    Testing_init_filestorage
    Testing_new
    Testing_save
    Testing_reload
    Testing_all
"""


import unittest
from models import storage
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel


class Testing_init_filestorage(unittest.TestCase):
    """ this tests the initializing class with the methods """

    def testing_file_storage(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def testing_file_storage_wargs(self):
        with self.assertRaises(TypeError):
            FileStorage("string arg")
        with self.assertRaises(TypeError):
            FileStorage(99, [])

    def testing_file_storage_woarg(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def testing_file_storage_path(self):
        with self.assertRaises(AttributeError):
            FileStorage().file_path

    def testing_private_file_storage_path(self):
        with self.assertRaises(AttributeError):
            FileStorage().__file_path

    def testing_file_storage_objects(self):
        with self.assertRaises(AttributeError):
            FileStorage().objects

    def testing_private_file_storage_objects(self):
        with self.assertRaises(AttributeError):
            FileStorage().__objects


class Testing_new(unittest.TestCase):
    """ this tests for new stored data class with these methods """

    def testin_new_stored_value(self):
        new_base = BaseModel()
        new_Fstore = FileStorage()
        new_Fstore.new(new_base)
        all_data = new_Fstore.all()
        key = "{}.{}".format(new_base.__class__.__name__, new_base.id)
        self.assertIs(new_base, all_data.get(key))

    def testin_new_stored_key(self):
        new_base = BaseModel()
        new_Fstore = FileStorage()
        new_Fstore.new(new_base)
        all_data = new_Fstore.all()
        key = "{}.{}".format(new_base.__class__.__name__, new_base.id)
        self.assertIsNotNone(all_data.get(key, None))

    def testing_stored_with_an_arg(self):
        self.assertIsNone(FileStorage().new(BaseModel()))

    def testing_stored_with_more_than_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().new({}, BaseModel())

    def testing_stored_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().new()


class Testing_save(unittest.TestCase):
    """ THis tests for the saved data class with these methods """

    @staticmethod
    def arrange():
        try:
            pass
        except BaseException:
            pass

    @staticmethod
    def erase():
        try:
            os.remove('object.json')
        except IOError:
            pass

    def testing_saved_with_more_than_an_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().save(BaseModel())

    def testing_saving_object(self):
        new_base = BaseModel()
        storage.save()
        with open('objects.json', 'r') as document:
            new_file = document.read()
            self.assertIn("BaseModel." + new_base.id, new_file)

    def testing_saving_app_file(self):
        pass

    def testing_saving_two_plus_file(self):
        pass


class Testing_all(unittest.TestCase):
    """ This tests for all data class with these methods """

    def testing_all(self):
        self.assertIsInstance(FileStorage().all(), dict)

    def testing_all_no_arg(self):
        self.assertIsNotNone(FileStorage().all())

    def testing_all_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().all({})
