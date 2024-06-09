import os
import psycopg2
from psycopg2.errors import *
from psycopg2.errorcodes import *
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv("DATABASE_NAME")
db_url = os.getenv("DATABASE_URL")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")


class Database:
    def __init__(self):
        self.db_connection = self.create_connection()
        self.cursor = self.db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    @staticmethod
    def create_connection():
        try:
            db_connection = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_url
            )
        except CLASS_CONNECTION_EXCEPTION as e:
            print(f"Error: failed to connect to db with error: {e.pgerror}\n")
            return False

        print(f"Connection to DB OK")
        return db_connection

    def execute_query_fetchone(self, query, args):
        print(f"execute_query_fetchone with query {query} and args {args}")
        try:
            self.cursor.execute(query, args)
            self.db_connection.commit()
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error: failed to execute query with error: {e}\n ")
            return False

    def execute_query_fetchall(self, query, args):
        print(f"execute_query_fetchall with query {query} and args {args}")
        try:
            self.cursor.execute(query, args)
            self.db_connection.commit()
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error: failed to execute query with error: {e}\n ")
            return False

    def execute_query_fetch_none(self, query, args):
        print(f"execute_query_fetch_none with query {query} and args {args}")
        try:
            self.cursor.execute(query, args)
            self.db_connection.commit()
            return True
        except Error as e:
            print(f"Error: failed to execute query with error: {e}\n ")
            return False




