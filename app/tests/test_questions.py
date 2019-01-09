import unittest
import json

#Local import
from app import create_app


class TestStackOverflow(unittest.TestCase):
    """ """
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.questions = {'title':'Python', 'body':'What is TDD', 'createdOn': '1800hrs', 'createdBy' : 1, 'meetup': 1, 'votes': 5,'meetup': 1}
     
    def test_post_question(self):
        """ Test posting a question."""
        response = self.client.post('/api/v1/post_question/', data=json.dumps(self.questions), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_downvote_a_question(self):
        """ Test editing a question."""
        response = self.client.patch('/api/v1/question/1/downvote/', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)    

    def test_upvote_a_question(self):
        """ Test editing a question."""
        response = self.client.patch('/api/v1/question/1/upvote/', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)    



if __name__ == '__main__':
    unittest.main()                    