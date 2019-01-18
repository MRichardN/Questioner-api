
from datetime import datetime
from .base_model import Model
from ..utils.utils import idGenerator

questions = []

class Question(Model):
    """ This class represents the class model """

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


'''
class Question:
    """
    This class represents the questions model.
    """
    def __init__(self, question_list):
        """
        Initialize questions list.
        """
        self.question_list = question_list

    def show_questions(self):
        """
        Show all questions.
        """
        return self.question_list

    def add_question(self, question):
        """
        Add questions to the list.
        """
        self.question_list.append(question)

    def update_question(self, index, createdOn, createdBy, meetup, title, body, votes):
        """
        Update a question.
        """
        new_question = [new_question for new_question in self.question_list if new_question["id"] == index]
        if new_question:
            new_question[0]["createdOn"] = createdOn
            new_question[0]["createdBy"] = createdBy
            new_question[0]["meetup"] = meetup
            new_question[0]["title"] = title
            new_question[0]["body"] = body
            new_question[0]["votes"] = votes
            return new_question[0]

    def delete_question(self, index):
        """
        Delete questions.
        """
        del_question = [del_question for del_question in self.question_list if del_question["id"] == index]
        if del_question:
            self.question_list.remove(del_question[0])
            return True

'''