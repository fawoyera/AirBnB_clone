#!/usr/bin/python3
""" This Modual contain the place class that inhertits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ This class defines the place modual and it attributes

    Attributes:
      city_id: City.id (string)
      user_id: User.id (string)
      name: Place name (string)
      description: Place description (string)
      number_rooms: Number of rooms (integer)
      number_bathrooms: Number of bathrooms (integer)
      max_guest: Number of max guest accepted at the place (integer)
      price_by_night: Price by night at the place (integer)
      latitude: Location latitude (float)
      longitude: Location longitude (float)
      amenity_ids: Available amenity at the place (Amenity.id) (list)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
