#!/usr/bin/env python3

""" this tests class in the file storage class as follows:

    Testing_init_filestorage
    Testing_new
    Testing_save
    Testing_reload
"""


import unittest
from models import storage
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel


class Testing_init_filestorage(unittest.TestCase):
    """ this tests the initializing class with the methods """
