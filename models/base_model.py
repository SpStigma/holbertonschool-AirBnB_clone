#!/usr/bin/python3

""" module base_module"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__})"
    
    def save(self):
        self.updated_at = datetime.now()
        return self.updated_at
    
    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat() if self.updated_at else None
        return data
