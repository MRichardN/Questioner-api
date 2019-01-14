from datetime import datetime
from .base_model import Model
from ..utils.utils import idGenerator

questions = []

class Question(Model):
    """ This class represents the class model."""

    def __init__(self):
        super().__init__(questions)

    def save(self, data):
        """ Save meetup."""
        data['id'] = idGenerator(self.collection)
        data['votes'] = 0
        return super().save(data)

    def upvote(self, question_id):
        """ upvote a question."""
        for question in questions:
            if question['id'] == question_id:
                question['votes'] = question['votes']+1
            return question    

    def downvote(self, question_id):
        """ Downvote a question."""
        for question in questions:
            if question['id'] == question_id:
                question['votes'] = question['votes']-1
            return question    
