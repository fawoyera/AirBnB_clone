#!/usr/bin/python3
""" Base Model Class """

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel

    Attributes:
       id: uuid of the model instance
       created_at: Time of the creation
       updated_at: Last time updated
    """

    # Initiaisation
    def __init__(self, *args, **kwargs):
        """ 
        Initialize BaseModel instance 
        
           *args : Will not be used
           **kwargs: arguments for the constructor of a BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    # Public Methodes
    def __str__(self):
        """ Return string representation of BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute updated_at with the current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary containing all the keys/values of __dict__ of the instance """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
