import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    """ Class represents Base test."""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None

    def registerUser(self):
        """ Register a new user."""
        
        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kingstone',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2108',
            'phoneNumber' : '0799999999'
        }

        response = self.client.post('/api/v1/register/', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
