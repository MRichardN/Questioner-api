import unittest
from app import create_app

class TestDevelopmentConfig(unittest.TestCase):
    """ Test development environment config."""

    def setUp(self):
        # Initialize development environment in app
        self.app = create_app('development')

    def test_development_environment(self):
        """ Test configuration in developmenet environment."""
        self.assertEqual(self.app.config['DEBUG'], True)  

    def tearDown(self):
        #Restore app to initial state
        self.app = None      

class TestTestingConfig(unittest.TestCase):
    """ Test testing environment config."""

    

class TestStagingConfig(unittest.TestCase):
    """ Test statging environment config."""

class TestProductionConfig(unittest.TestCase):
    """ Test production environment config."""    