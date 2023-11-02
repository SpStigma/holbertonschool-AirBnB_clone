#!/usr/bin/python3

"""module review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a user's review of a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
