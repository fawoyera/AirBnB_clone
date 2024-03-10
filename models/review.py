#!/usr/bin/python3
""" This Modual contain the review class that inhertits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class defines the review modual and it attributes

    Attributes:
      place_id: Place.id (string)
      user_id: User.id (string)
      text: Review comment (string)
    """
    place_id = ""
    user_id = ""
    text = ""
