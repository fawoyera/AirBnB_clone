#!/usr/bin/python3
""" This Modual contain the city class that inhertits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This class defines the city modual and it attributes 
    
    Attributes:
      state_id: state.id (string)
      name: name of city (string)
    """
    state_id = ""
    name = ""
