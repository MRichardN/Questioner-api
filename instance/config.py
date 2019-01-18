"""
    Configuration
"""
import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET_KEY')
    DATABASE_HOST = os.getenv('DB_HOST')
    DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE_USERNAME = os.getenv('DB_USERNAME')



class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_NAME = os.getenv('DEV_DB_NAME')


class TestingConfig(Config):
    """Configurations for Testing; with a separate test database."""
    TESTING = True
    DEBUG = True
    DATABASSE_NAME = os.getenv('TEST_DB')


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}
