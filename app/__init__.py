
"""
Main file.
"""
#Third party import
from flask import Flask

#Local import
from instance.config import app_config
#import instance.config.app_config
from app.api.v1.views.views import version1



def create_app(config_name):
    """
    Create app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(version1)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app
