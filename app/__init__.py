
"""
Main file.
"""
import datetime
#Third party import
from flask import Flask
from flask_jwt_extended import JWTManager

#Local import
from instance.config import app_config
from app.api.v1.views.user_views import version1 as usersBlueprint
from app.api.v1.views.meetup_views import version1 as meetupsBlueprint
from app.api.v1.views.question_views   import version1 as questionsBlueprint



def create_app(config_name):
    """
    Create app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(version1)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # register Version1 blueprints
    app.register_blueprint(usersBlueprint)
    app.register_blueprint(meetupsBlueprint)
    app.register_blueprint(questionsBlueprint)

     # JWT    
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']    
    app.config['JWT_SECRET_KEY'] = 'yuiopkkv'
    app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
    jwt = JWTManager(app)
    @jwt.token_in_blacklist_loader
    def check_blacklisted(decrypted_token):
        from app.api.v1.models.token_model import RevokedTokenModel
        jti = decrypted_token['jti']
        return RevokedTokenModel().inBlacklist(jti)


    return app
