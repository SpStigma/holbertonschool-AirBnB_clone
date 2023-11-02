#!/usr/bin/python3

"""module city """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city within a specific state.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
