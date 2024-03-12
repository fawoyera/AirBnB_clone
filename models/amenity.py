#!/usr/bin/python3
""" This Modual contain the amenity class that inhertits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This class defines the amenity modual and it attributes

    Attributes:
      name : name of the amenity
    """
    name = ""
