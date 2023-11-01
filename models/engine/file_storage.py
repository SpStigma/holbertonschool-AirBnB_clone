#!/usr/bin/python3

""" module file_storage"""
import json


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects
    

    def new(self, obj):
        """
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """
        """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)


    def reload(self):
        """
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj = cls(**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
