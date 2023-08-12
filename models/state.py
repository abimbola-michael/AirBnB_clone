#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """class User that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Class Initalization"""

        super().__init__(**kwargs)
