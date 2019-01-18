from werkzeug.security import generate_password_hash

tables = [
    'users',
    'meetups',
    'questions',
    'comments'
]

table_queries = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY NOT NULL,
        firstname VARCHAR(250) NOT NULL,
        lastname VARCHAR(250) NOT NULL,
        othername VARCHAR(250) NULL,
        username VARCHAR(250) NOT NULL,
        phonenumber VARCHAR(250) NULL,
        email VARCHAR(250) NOT NULL,
        password VARCHAR(250) NOT NULL,
        registered TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        admin BOOLEAN NOT NULL DEFAULT FALSE
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS meetups (
        id SERIAL PRIMARY KEY NOT NULL,
        topic VARCHAR(250) NOT NULL,
        description VARCHAR(250) NOT NULL,
        location VARCHAR(250) NOT NULL,
        happening_on VARCHAR(250) NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc')
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY NOT NULL,
        topic VARCHAR(250) NULL,
        body VARCHAR(250) NOT NULL,
        votes INTEGER NOT NULL DEFAULT 0,
        meetup_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (meetup_id) REFERENCES meetups(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS comments (
        id SERIAL PRIMARY KEY NOT NULL,
        body VARCHAR(250) NULL,
        question_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (question_id) REFERENCES questions(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
]


def truncate(connection):
    """ Function to truncate database tables """

    cur = connection.cursor()
    cur.execute('TRUNCATE TABLE ' + ','.join(tables) + ' CASCADE')
    connection.commit()


def drop_tables(connection):
    """ Function to drop tables """

    cur = connection.cursor()
    for table in tables:
        cur.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table))

    connection.commit()


def create_tables(connection):
    """ Function to create tables """

    cur = connection.cursor()
    for query in table_queries:
        cur.execute(query)

    connection.commit()


def seed(connection):
    cur = connection.cursor()
    cur.execute("INSERT INTO users (firstname, lastname, username, email, password, admin)\
        VALUES ('Vincent', 'Tirgei', 'tirgei', 'admin@app.com', '{}', True)\
        ".format(generate_password_hash('asf8$#Er0')))
    connection.commit()


'''
class Tables(object):
    
    def table_users(self, connection):
        """ create users table."""
        query = """CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        username VARCHAR(30) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(120) NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        phoneNumber VARCHAR(50) NULL,
        registered TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
        isAdmin BOOLEAN NOT NULL DEFAULT FALSE      
                
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def table_questions(connection):
        query = """CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
        createdBy VARCHAR(50) NOT NULL,
        title VARCHAR(250) NULL,
        body VARCHAR(250) NOT NULL,
        votes INTEGER NOT NULL DEFAULT 0,
        meetup_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (meetup_id) REFERENCES meetups(id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE

        )""" 
        cur = connection.cursor()
        cur.execute(query) 
        connection.commit() 

    def table_meetups( connection):
        query = """CREATE TABLE IF NOT EXISTS meetups (
        id SERIAL PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
        location VARCHAR(250) NOT NULL,
        images VARCHAR(256)
        topic VARCHAR(256) NOT NULL,
        happeningOn TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
        description VARCHAR(250) NOT NULL,
        tags VARCHAR(256)
        )"""
        cur = connection.cursor()
        cur.execute(query)  
        connection.commit() 

    def table_comments(self, connection):
        query = """CREATE TABLE IF NOT EXISTS comments(
        id SERIAL PRIMARY KEY NOT NULL,
        description VARCHAR(256) NULL,
        createdOn TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
        question_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE

        )"""
        cur = connection.cursor()
        cur.execute(query)  
        connection.commit()      
        '''