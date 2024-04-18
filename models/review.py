#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information """

    def __init__(self, *args, **kwargs):
        """ Initializes a Review instance """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    place_id: str  # ID of the place being reviewed
    user_id: str  # ID of the user who created the review
    text: str  # Text content of the review

