class Questions():
    
    

    
    def add_question(self, title, description, time_created,userid, cursor):
        "add question to the database in user table"
        query="""INSERT INTO questions(title,description,time_created,userid) VALUES(%s,%s,%s,%s)
        """
        cursor.execute(query,(title,description,time_created, userid))
        return cursor

    def update_question(self, title, description, questionid, cursor):
        "update question details in the database"
        query="UPDATE questions SET title=%s, description=%s WHERE questionid=%s;"
        cursor.execute(query,(title,description,questionid))
        return cursor

    def delete_question(self,questionid,cursor):
        "delete question by id"
        query="DELETE FROM questions WHERE questions.questionid = %s"
        cursor.execute(query,(questionid,))
        return cursor

    def search_question_by_title(self,title,cursor):
        "search question by title"
        query="SELECT * FROM questions WHERE title Like %s"
        cursor.execute(query,(title,))
        return cursor

    def search_question_by_questionid(self,questionid,cursor):
        "search question by id"
        query="SELECT * FROM questions WHERE questionid = %s"
        cursor.execute(query,(questionid,))
        return cursor

    def search_question_by_user(self,userid, cursor):
        query="SELECT * FROM questions WHERE userid = %s"
        cursor.execute(query,(userid,))
        return cursor

    def fetch_all_question(self, cursor):
        "fetchall questions"
        query = "SELECT * FROM questions"
        cursor.execute(query)
        return cursor

    def clear_question_table(self,connection):
        "clear user table"
        query ="""DROP TABLE questions CASCADE"""
        cursor = connection.cursor()
        cursor.execute(query)    