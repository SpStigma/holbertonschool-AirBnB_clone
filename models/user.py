#!/usr/bin/python3

"""module user"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents a registered user in the system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Inherits:
        BaseModel: The base model class providing common attributes and methods
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
