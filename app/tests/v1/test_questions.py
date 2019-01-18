# third party import
from flask import json

# local import
from .base_test import BaseTest
from app.api.v1.models.questions_model import questions

class TestQuestions(BaseTest):
    """ This class tests questions."""

    def setUp(self):
        """ setup."""
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}

    def tearDown(self):
        """ Restore to initial state """
        questions.clear()
        super().tearDown()

    def test_post_question_without_data(self):
        """ Test post empty data """
        res = self.client.post('/api/v1/post_question/')
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data sent')

    def test_post_question_without_entries(self):
        """ empty."""
        question = {}

        res = self.client.post('/api/v1/post_question/', json=json.dumps(question), headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please enter all fields')

    def test_post_question_with_missing_fields(self):
        """ Test post question with missing fields."""
        
        question = {
            'title' : 'Postgress DB'
        }

        res = self.client.post('/api/v1/post_question/', json=question, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please enter all fields')

    def test_post_question(self):
        """ post question."""
        question = {
            'title': 'Postgress Database',
            'body':'asdfutyretbj',
            'meetup' : 1,
            'createdBy': 1
        }

        res = self.client.post('/api/v1/post_question/', json=question, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['Success'], 'Question created successfully')

    def test_upvote_question_nonexistent_question(self):
        """ Test upvote not found question """
        res = self.client.patch('/api/v1/question/93/upvote/')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'Question not found')

    def test_upvote_existing_question(self):
        """ Test upvote."""
        question = {
            'title': 'Postgress Database',
            'body':'asdfutyretbj',
            'meetup' : 1,
            'createdBy': 1
        }

        res_post = self.client.post('/api/v1/post_question/', json=question, headers=self.headers)
        question_id = res_post.get_json()['data']['id']

        res = self.client.patch('/api/v1/question/{}/upvote/'.format(question_id))
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Quesion up-voted')
        self.assertEqual(data['data']['votes'], 1)


    def test_downvote_existing_question(self):
        """ Test downvote."""
        question = {
            'title': 'Postgress Database',
            'body':'asdfutyretbj',
            'meetup' : 1,
            'createdBy': 1
        }

        res_post = self.client.post('/api/v1/post_question/', json=question, headers=self.headers)
        question_id = res_post.get_json()['data']['id']

        res = self.client.patch('/api/v1/question/{}/downvote/'.format(question_id))
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Quesion down-voted')
        self.assertEqual(data['data']['votes'], -1)

#pending tests


    def test_downvote_noon_existent_question(self):
        """ Test downvote question not found."""
        res = self.client.patch('/api/v1/question/2295/downvote/')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'Question not found')
      