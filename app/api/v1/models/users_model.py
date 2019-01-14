from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#local import
from .base_model import Model
from ..utils.utils import idGenerator

users = []

class User(Model):
    """" This class represents users model."""
    def __init__(self, ):
        super().__init__(users)

    def save(self, data):
        """ Save a new user."""
        data['id'] = idGenerator(self.collection)
        data['password'] = generate_password_hash(data['password'])
        data['isAdmin'] = False
        return super().save(data)

    def checkpasswordhash(self, pwd_hash, password):
        """ Check password match with its hash."""
        return check_password_hash(pwd_hash, password)    