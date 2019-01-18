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
        """ Save a new user """
        data['id'] = idGenerator(self.collection)
        data['password'] = generate_password_hash(data['password'])
        data['isAdmin'] = False
        return super().save(data)

    def checkpasswordhash(self, hash, password):
        """ Check password match."""
        return check_password_hash(hash, password)    




'''
if len(collection) == 0:
        return 1
    else:
        return collection[-1]['id']+1

class User:
    """
    This class represents the users model.
    """
    def __init__(self, user_list):
        """
        Initialize user list.
        """
        self.user_list = user_list

    def add_user(self, user):
        """
        Add questions to the list.
        """
        self.user_list.append(user)

    def update_user(self, index, firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin):
        """
        Update a user.
        """
        new_user = [new_user for new_user in self.user_list if new_user["id"] == index]
        if new_user:
            new_user[0]["firstname"] = firstname
            new_user[0]["lastname"] = lastname
            new_user[0]["othername"] = othername
            new_user[0]["email"] = email
            new_user[0]["phoneNumber"] = phoneNumber
            new_user[0]["username"] = username
            new_user[0]["registered"] = registered
            new_user[0]["isAdmin"] = isAdmin
            return new_user[0]


class Admin(User):
    """
        This class represents the Admin and inherits User.
    """
    def __init__(self, name):
        User.__init__(self, name)
    
    def can_create(self):
        return True

    def can_edit(self):
        return True

    def can_delete(self):
        return True    
'''