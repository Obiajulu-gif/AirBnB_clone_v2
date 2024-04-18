#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """ A place to stay """

    def __init__(self, *args, **kwargs):
        """ Initializes a Place instance """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []  # List of amenity IDs

    city_id: str  # City ID where the place is located
    user_id: str  # User ID who owns the place
    name: str  # Name of the place
    description: str  # Description of the place
    number_rooms: int  # Number of rooms in the place
    number_bathrooms: int  # Number of bathrooms in the place
    max_guest: int  # Maximum number of guests the place can accommodate
    price_by_night: int  # Price per night for the place
    latitude: float  # Latitude coordinate of the place
    longitude: float  # Longitude coordinate of the place
    amenity_ids: List[str]  # List of amenity IDs associated with the place

