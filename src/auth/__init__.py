from uuid import uuid4
from src.globals import *


class Auth:

    def __init__(self, db):
        self.db = db

    def authenticate_token(self, username, device_id, token):
        print("auth.authenticate_token")
        query_args = (username, device_id, token)
        return self.db.execute_query_fetchone(AUTH_TOKEN_QUERY, query_args)

    def authenticate_login(self, username, password, device_id):
        print("auth.authenticate_login")
        query_args = (username, password)
        return self.create_user_token(username, device_id) \
            if self.db.execute_query_fetchone(AUTH_LOGIN_QUERY, query_args) \
            else False

    def register_user(self, username, mobile, password):
        print("auth.register_user")
        query_args = (username, mobile, password)
        return self.db.execute_query_fetch_none(AUTH_REGISTER_QUERY, query_args)

    def validate_user_exists(self, mobile):
        print("auth.validate_user_exists")
        query_args = (mobile,)
        return self.db.execute_query_fetchone(AUTH_USER_EXISTS_QUERY, query_args)

    def create_user_token(self, username, device_id):
        print("auth.create_user_token")
        token = str(uuid4().hex)
        query_args = (username, device_id, token)
        return token if self.db.execute_query_fetch_none(AUTH_CREATE_TOKEN_QUERY, query_args) else False

    def logout_user(self, username, device_id, token):
        print("auth.logout_user")
        query_args = (username, device_id, token)
        return self.db.execute_query_fetch_none(AUTH_DELETE_TOKEN_QUERY, query_args)

    def delete_user(self, username, mobile):
        print("auth.delete_user")
        query_args = (username, mobile)
