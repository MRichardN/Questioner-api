

import os
import psycopg2
from instance.config import app_config


config_name = os.getenv('APP_ENV')
config = app_config[config_name]


def db_conn():
    """ DB connection string."""
    database = config.DEV_DB_NAME
    host = config.DB_HOST
    user = config.DB_USERNAME
    password = config.DB_PASSWORD
    

    db_url = 'dbname={} host={} user={} password={}'.format(database, host, user, password)

    try:
        conn = psycopg2.connect(db_url)

    except (Exception, psycopg2.Error) as e:
        print('Unable to connect to the database', e)
       

    return conn  






'''
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

'''        