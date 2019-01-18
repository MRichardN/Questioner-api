from datetime import datetime
from ..utils.utils import idGenerator
from .base_model import Model

meetups = []

class Meetup(Model):
    """ This class represents the meetup model."""

    def __init__(self):
        super().__init__(meetups)

    def save(self, data):
        """ Save a meetup."""
        data['id'] = idGenerator(self.collection)
        data['createdOn'] = datetime.now()
        data['happeningOn'] = datetime.now()
        return super().save(data)

   



   



