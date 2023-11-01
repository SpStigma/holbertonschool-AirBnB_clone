#!/usr/bin/python3

""" module file_storage"""
import json
import os


class FileStorage:

    """
    This class handles the storage and retrieval of objects in a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all currently loaded objects.

        Returns:
            dict: A dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves all objects to the JSON file.
        """
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Loads objects from the JSON file and populates the storage.
        """
        from models import base_model

        module_mapping = {
            "BaseModel": base_model
        }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:

                data = json.load(file)

                for key, value in data.items():
                    class_name = value["__class__"]

                    if class_name in module_mapping:
                        model_module = module_mapping[class_name]
                        model_class = getattr(model_module, class_name)

                    obj_instance = model_class(**value)
                    self.__objects[key] = obj_instance
