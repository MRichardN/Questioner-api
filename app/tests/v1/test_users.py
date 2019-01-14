# third party import
from flask import json

# local import
from app.api.v1.models.users_model import users
from .base_test import BaseTest

class TestUser(BaseTest):
    """ Test class for user endpoints."""

    def setUp(self):
        """ Initialize."""
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}

    def tearDown(self):
        """ Restore to initial state."""
        users.clear()
        super().tearDown()

    

    def test_register_with_no_data(self):
        """ Test register user with no data sent."""
        res = self.client.post('/api/v1/register/')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_register_with_empty_entries(self):
        """ Test register user with blank credentials """
        user = {}
        res = self.client.post('/api/v1/register/', json=json.dumps(user), headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')

    def test_register_with_missing_fields(self):
        """ Test register with missing fields."""
        user = {
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2108',
            'phoneNumber' : '0799999999'
        }

        res = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'],  'Invalid data. Please fill all required fields')

    def test_register_with_invalid_email(self):
        """ Test register with invalid email."""

        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Oyaro',
            'username' : 'OyaroD',
            'email' : 'johndoe.com',
            'password' : '123qwe',
            'phone_number' : '0799999999'
        }

        res = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')

    def test_register_with_invalid_password(self):
        """ Test register with invalid password """

        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : '00000',
            'phoneNumber' : '0799999999'
        }

        res = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')

    def test_register_with_correct_credentials(self):
        """ Test register_user with correct credentials."""

        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2020',
            'phoneNumber' : '0799999999'
        }

        res = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'New user created ')
        self.assertEqual(data['data']['username'], user['username'])

    def test_register_with_existing_username(self):
        """ Test register with an existing username."""

        # Create the first new user
        user1 = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2020',
            'phoneNumber' : '0799999999'
        }

        res1 = self.client.post('/api/v1/register/', json=user1, headers=self.headers)
        data1 = res1.get_json()

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(data1['status'], 201)
        self.assertEqual(data1['message'], 'New user created ')

        # Create a second new_user with similar username
        user2 = {
            'firstname' : 'James',
            'lastname' : 'Doe',
            'othername' : 'Ouko',
            'username' : 'JohnDoe',
            'email' : 'jamesouko@gmail.com',
            'password' : 'James@2020',
            'phoneNumber' : '0788888888'
        }
        res2 = self.client.post('/api/v1/register/', json=user2, headers=self.headers)
        data2 = res2.get_json()

        self.assertEqual(res2.status_code, 409)
        self.assertEqual(data2['status'], 409)
        self.assertEqual(data2['message'], 'Username already exists')

    def test_register_existing_username(self):
        """ Test sign up with an existing email."""

         # Create the first new user
        user1 = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2020',
            'phoneNumber' : '0799999999'
        }

        res1 = self.client.post('/api/v1/register/', json=user1, headers=self.headers)
        data1 = res1.get_json()

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(data1['status'], 201)
        self.assertEqual(data1['message'], 'New user created ')

        # Create a second new_user with similar email
        user2 = {
            'firstname' : 'James',
            'lastname' : 'Doe',
            'othername' : 'Ouko',
            'username' : 'JohnDoe',
            'email' : 'jamesdoe@gmail.com',
            'password' : 'James@2020',
            'phoneNumber' : '0788888888'
        }

        res2 = self.client.post('/api/v1/register/', json=user2, headers=self.headers)
        data2 = res2.get_json()

        self.assertEqual(res2.status_code, 409)
        self.assertEqual(data2['status'], 409)
        self.assertEqual(data2['message'], 'Username already exists')

    def test_login_no_data_sent(self):
        """ Test login with no data sent """
        res = self.client.post('/api/v1/login/')
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    

    def test_login_unregistered_user(self):
        """ Test login with unregistered user credentials """
        user = {
            'username' : 'Jacob',
            'password' : 'asdfg123A@'
        }
        res = self.client.post('/api/v1/login/', json=user, headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'User not found')

    def test_valid_login(self):
        """ Test a valid login."""
        # Register a new user
        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2020',
            'phoneNumber' : '0799999999'
        }

        res1 = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data1 = res1.get_json()
        self.assertEqual(res1.status_code, 201)
        self.assertEqual(data1['status'], 201)
        self.assertEqual(data1['message'], 'New user created ')

        # Login user
        user2 = {
            'username':'JohnDoe',
            'password':'John@2020'
        }
        res2 = self.client.post('/api/v1/login/', json=user2, headers={'Content-Type': 'application/json'})
        data2 = res2.get_json()

        self.assertEqual(res2.status_code, 200)
        self.assertEqual(data2['status'], 200)
        self.assertEqual(data2['message'], 'User logged in successfully')

    def test_login_without_username_provided(self):
        """ Test login with no username provided."""
        # Register user
        user = {
            'firstname' : 'John',
            'lastname' : 'Doe',
            'othername' : 'Kamau',
            'username' : 'JohnDoe',
            'email' : 'johndoe@gmail.com',
            'password' : 'John@2020',
            'phoneNumber' : '0799999999'
        }

        res1 = self.client.post('/api/v1/register/', json=user, headers=self.headers)
        data1 = res1.get_json()
        self.assertEqual(res1.status_code, 201)
        self.assertEqual(data1['status'], 201)

        # Login user
        res2 = self.client.post('/api/v1/login/', json={'password': 'JohnD@2020'}, headers=self.headers)
        data2 = res2.get_json()
        self.assertEqual(res2.status_code, 400)
        self.assertEqual(data2['status'], 400)
        self.assertEqual(data2['message'], 'Invalid credentials')   


