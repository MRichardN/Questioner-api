"""this model is intede to perform all the user functions"""
#from .database import db_conn
#import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

class Users(object):
    """Users."""
    #taable users
    def register_user(self, firstname, lastname, username, email, password, phoneNumber, cursor):
        """ create new user."""
        query = """INSERT INTO users(firstname, lastname, username, email,password, phoneNumber) \
        VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (firstname, lastname, username, email, generate_password_hash(password), phoneNumber))
        return cursor

    def update_user(self, userid, username, email, password, cursor):
        """ update user details."""
        query = "UPDATE users SET username=%s, email=%s, password=%s WHERE userid=%s"
        cursor.execute(query, (username, email, password, userid))
        return cursor

    def clear_user_table(self, connection):
        """clear everything in user table."""
        query = """DROP TABLE users  CASCADE"""
        connection.cursor.execute(query)

    @staticmethod
    def checkpassword(hashed_pwd, pwd):
        """ check if passwords match."""

        return check_password_hash(hashed_pwd, pwd)    




    

