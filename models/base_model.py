#!/usr/bin/python3
"""
Module contains the BaseModel class
"""
import uuid
import datetime


class BaseModel:
    """
    class BaseModel defines all common attributes/methods for other \
classes:

    Public instance attributes:
        - id: this is a unique uuid for an instance
        - created_at: datetime when an instance is created
        - updated_at: datetime everytime an instance is updated

    Public instance methods:
        - save(self): updates the public instance attribute updated_at with \
the current datetime
        - to_dict(self): returns a dictionary containing all keys/values of \
__dict__ of the instance
    """
    def __init__(self):
        """
        Function is called whenever an instance is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns the string representation of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with \
the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ \
of the instance
        """
        dict_repr = self.__dict__
        for key, value in dict_repr.items():
            if type(dict_repr[key]) is datetime.datetime:
                dict_repr[key] = value.isoformat()
        dict_repr["__class__"] = type(self).__name__
        return dict_repr