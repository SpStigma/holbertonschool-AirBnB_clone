#!/usr/bin/python3

""" module base_module"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Represents a base model with a unique identifier, creation timestamp, and
    update timestamp.

    Attributes:
        id (str): A unique identifier generated using UUID4.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last
        updated (initialized to the creation time).

    Methods:
        __init__(): Initializes a new instance of BaseModel.
        __str__(): Returns a string representation of the BaseModel instance.
        save(): Updates the 'updated_at' attribute with the current date and
        time.
        to_dict(): Converts the BaseModel instance to a dictionary
        representation.
    """
    def __init__(self):
        """
        Initializes a new instance of BaseModel.

        Attributes:
            id (str): A unique identifier generated using UUID4.
            created_at (datetime): The date and time when the instance
            was created.
            updated_at (datetime): The date and time when the instance was
            last updated (initialized to the creation time).
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A formatted string indicating the class name, id, and the
            instance's dictionary representation.
        """
        return f"[BaseModel] ({self.id}) {self.__dict__})"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time.

        Returns:
            datetime: The updated date and time in 'datetime' format.
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance's attributes and their
            values, including class name, creation time, and update time.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
