import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    """ Class represents Base test."""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        # restore to initial state
        self.app = None

    