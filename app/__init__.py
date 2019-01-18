
"""
Main file.
"""
import os
import datetime

#Third party import
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

#Local import
from instance.config import app_config
from app.api.v1.views.user_views import version1
from app.api.v2 import version2 
from app.api.v2.util.db_config import db_conn
#from app.api.v2.util.tables import Tables
from app.api.v2.util.tables import create_tables, seed


def create_app(config_name):
    """Initialize  app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])    
    app.config.from_pyfile('config.py')

    # register Version1 blueprints
    app.register_blueprint(version1)
    app.register_blueprint(version2)

    # JWT
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']    
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
    jwt = JWTManager(app)
    @jwt.token_in_blacklist_loader
    def check_blacklisted(decrypted_token):
        from app.api.v1.models.token_model import RevokedTokenModel
        jti = decrypted_token['jti']
        return RevokedTokenModel().inBlacklist(jti)
    
    #db
    conn = db_conn()
    create_tables(conn)
    seed(conn)

    
        
    

    return app
