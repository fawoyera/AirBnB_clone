#!/usr/bin/python3
""" This Modual contain the state class that inhertits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This class defines the state modual and it attributes 
    
    Attributes:
      name: state name (string)
    """
    name = ""
