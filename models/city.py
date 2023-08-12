#!/usr/bin/python3
# class City that inherits from BaseModel

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class Initalization"""

<<<<<<< HEAD
        super().__init__(**kwargs)
=======
        super().__init__(*args, **kwargs)
>>>>>>> 75c8da719079a53507a8143a42b4660de5fd3c93
