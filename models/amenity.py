#!/usr/bin/python3

"""module amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a type of facility or feature that
    a place may have.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
