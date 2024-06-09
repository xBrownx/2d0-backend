from src.globals import *


class Users:

    def __init__(self, db):
        self.db = db

    def validate_request_params(self):
        try:
            username = self.request.json.get('username')
            mobile = self.request.json.get('mobile')
            password = self.request.json.get('password')
        except Error as e:
            self.response[RESULT] = False
            self.response[MSG] = f"Error: Failed to parse json from request. {e}"
            print(self.response)
            return False

        if not username or not mobile or not password:
            self.response[RESULT] = False
            self.response[MSG] = "Error: Required field 'email' or 'mobile' were empty"
            print(self.response)
            return False

        if self.validate_user(mobile):
            self.response[RESULT] = False
            self.response[MSG] = "Error: User with mobile number already exists"
            print(self.response)
            return False

        return username, mobile, password


