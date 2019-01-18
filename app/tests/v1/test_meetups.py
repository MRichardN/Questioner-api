# third party imports
from flask import json

# local imports
from app.api.v1.models.meetups_model import meetups
from .base_test import BaseTest


class TestMeetups(BaseTest):
    """ Test class for meetup endpoints """

    def setUp(self):
        """ Initialize requirements for meetup tests."""
        self.headers = {'Content-Type': 'application/json'}
        super().setUp()     
        
    def tearDown(self):
        """ Reinitalize to initial state."""
        meetups.clear()
        super().tearDown()

    def test_post_meetup_with_no_data(self):
        """ Test post meetup with no data."""
        res = self.client.post('/api/v1/post_meetup/')
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Failed: No data provided')

    def test_create_meetup_with_empty_data(self):
        """ Test create meetup with no data sent."""
        meetup = {}
        res = self.client.post('/api/v1/post_meetup/', json=json.dumps(meetup), headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please enter all required fields')

    def test_create_meetup_missing_fields(self):
        """ Test create meetup with missing fields."""
        # Create meetup without topic
        meetup = {
            'location' : 'Andela',
            'happeningOn' : 'January 13, 2019'
        }

        res = self.client.post('/api/v1/post_meetup/', json=json.dumps(meetup), headers=self.headers)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please enter all required fields')

   
    def test_rsvps_meetup_not_created(self):
        """ Test rsvp non existent rsvp."""
        res = self.client.post('/api/v1/meetups/4/maybe/')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Meetup does not exist')

    def test_create_meetup(self):
            """ Test create meetup."""
            meetup = {
                'topic' : 'Postgress Database',
                'location' : 'Andela',
                
                'happeningOn' : 'Jan 14, 2019'
            }

            res = self.client.post('/api/v1/post_meetup/', json=meetup, headers=self.headers)
            data = res.get_json()
            self.assertEqual(res.status_code, 201)
            self.assertEqual(data['status'], 201)
            self.assertEqual(data['message'], 'Meetup created')

    
    def test_invalid_rsvp(self):
        """ Test rsvp for meetup that does not exist."""
        meetup = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',           
            'happeningOn' : 'Jan 16 ,2019',
            'tags' : ['python', 'validation']
        }
        self.client.post('/api/v1/post_meetup/', json=meetup, headers=self.headers)
        
        res = self.client.post('/api/v1/meetups/1/notSure/')
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid rsvp')

    def test_valid_rsvp_for_yes(self):
        """ Test a valid rsvp for meetup (yes) ."""
        meetup = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',           
            'happeningOn' : 'Jan 16 ,2019',
            'tags' : ['python', 'validation']
        }
        res = self.client.post('/api/v1/post_meetup/', json=meetup, headers=self.headers)
        print(res.data)
        res = self.client.post('/api/v1/meetups/1/yes/')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Responded successfully')
    
    def test_valid_rsvp_for_no(self):
        """ Test a valid rsvp for meetup (no) ."""
        meetup = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',           
            'happeningOn' : 'Jan 16 ,2019',
            'tags' : ['python', 'validation']
        }
        res = self.client.post('/api/v1/post_meetup/', json=meetup, headers=self.headers)
        print(res.data)
        res = self.client.post('/api/v1/meetups/1/no/')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Responded successfully')

    def test_valid_rsvp_for_maybe(self):
        """ Test a valid rsvp for meetup (maybe) ."""
        meetup = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',           
            'happeningOn' : 'Jan 16 ,2019',
            'tags' : ['python', 'validation']
        }
        res = self.client.post('/api/v1/post_meetup/', json=meetup, headers=self.headers)
        print(res.data)
        res = self.client.post('/api/v1/meetups/1/maybe/')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Responded successfully')    

    def test_get_a_meetup_not_in_meetups(self):
        """ Test get a meetup that does not exist."""
        res = self.client.get('/api/v1/meetups/53/')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'Meetup does not exist')

    def test_get_all_meetups(self):
        """ Test get all meetups """
        # Create meetups
        meetup1 = {
            'topic' : 'Postgress Database',
            'location' : 'Andela',            
            'happeningOn' : 'Jan 15, 2019',
            'tags' : ['python', 'postgress']
        }
        meetup2 = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',
            'happeningOn' : 'Jan 16 ,2019',
            'tags' : ['python', 'validation']
        }
        self.client.post('/api/v1/post_meetup/', json=meetup1, headers=self.headers)
        self.client.post('/api/v1/post_meetup/', json=meetup2, headers=self.headers)
        res = self.client.get('/api/v1/meetups/upcoming/')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(len(data['result']), 2)      

    def test_get_a_specific_meetup(self):
        """ Test get a specific meetup."""
        # Create meetups
        meetup1 = {
            'topic' : 'Postgress Database',
            'location' : 'Andela',
            'happeningOn':'kenta',
            'tags' : ['python', 'postgress']
        }
        meetup2 = {
            'topic' : 'validations using JWT',
            'location' : 'Andela',
            'happeningOn': 'Kenya',
            'tags' : ['python', 'validation']
        }
        self.client.post('/api/v1/post_meetup/', json=meetup1, headers=self.headers)
        self.client.post('/api/v1/post_meetup/', json=meetup2, headers=self.headers)

        res = self.client.get('/api/v1/meetups/1/')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data']['id'], 1)

    