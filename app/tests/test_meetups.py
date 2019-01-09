import unittest
import json

from app import create_app


class TestStackOverflow(unittest.TestCase):
    """ """
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.meetups = { 'createdOn': '1800hrs', 'location': 'Here','topic': 'TDD', 'happeningOn': 'PAC','meetup': 1,'user': 1,'response': "some response"}
        

    def test_view_all_upcoming_meetups(self):
        """ Test view_all meetups."""
        response = self.client.get('/api/v1/meetups/upcoming/', content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_get_specific_meetup(self):
        """ Test view a single meetup."""
        response = self.client.get('/api/v1/meetups/1/', data=json.dumps(self.meetups), content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_post_meetup(self):
        """ Test posting a meetup."""
        response = self.client.post('/api/v1/post_meetup/', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete_meetup(self):
        """ Test deleting a meetup."""
        response = self.client.post('/api/v1/delete_meetup/1/', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertTrue(response.status_code, 200)  

    def test_post_rsvp(self):
        """ Test posting a rsvp."""
        response = self.client.post('/api/v1/meetups/1/rsvp/', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    


if __name__ == '__main__':
    unittest.main()                        

