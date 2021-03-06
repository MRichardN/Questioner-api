""" Testing config."""

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

    def setUp(self):
        # Initialize testing environment in app
        self.app = create_app('testing')

    def test_testing_environment(self):
        """ Test configuration in testing environment."""
        self.assertEqual(self.app.config['DEBUG'], True) 
        self.assertEqual(self.app.config['TESTING'], True) 

    def tearDown(self):
        #Restore app to initial state
        self.app = None

    

class TestStagingConfig(unittest.TestCase):
    """ Test statging environment config."""

    def setUp(self):
        # Initialize staging environment in app
        self.app = create_app('staging')

    def test_staging_environment(self):
        """ Test configuration in staging environment."""
        self.assertEqual(self.app.config['DEBUG'], True)

    def tearDown(self):
        #Restore app to initial state
        self.app = None

class TestProductionConfig(unittest.TestCase):
    """ Test production environment config.""" 

    def setUp(self):
        # Initialize production environment in app
        self.app = create_app('production')

    def test_production_environment(self):
        """ Test configuration in production environment."""
        self.assertEqual(self.app.config['DEBUG'], False)
        self.assertEqual(self.app.config['TESTING'], False)

    def tearDown(self):
        #Restore app to initial state
        self.app = None   