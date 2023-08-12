#!/usr/bin/python3
""" class City that inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class Initalization"""

        super().__init__(**kwargs)
