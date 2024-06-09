from psycopg2.errors import *
from psycopg2.errorcodes import *

from src.database import Database
from src.auth import Auth
from src.groups import Groups
from src.tasks import Tasks
from src.friends import Friends
from src.globals import *


class RequestPilot:

    def __init__(self, request):
        self.request = request
        self.db = Database()
        self.request_params = self.validate_request_params()

    def validate_request_params(self):
        print("main.validate_request_params")
        try:
            username = self.request.json.get(USERNAME)
            mobile = self.request.json.get(MOBILE)
            password = self.request.json.get(PASSWORD)
            token = self.request.json.get(TOKEN)
            device_id = self.request.json.get(DEVICE_ID)
        except Error as e:
            return {
                STATUS: False,
                ERROR: e
            }

        return {
            STATUS: True,
            USERNAME: username,
            MOBILE: mobile,
            PASSWORD: password,
            TOKEN: token,
            DEVICE_ID: device_id
        }

    def response_builder(self,result, token=None, msg=None, data=None):
        print("main.response_builder")
        return {
            USERNAME: self.request_params[USERNAME],
            TOKEN: token,
            RESULT: result,
            MSG: msg,
            DATA: data
        }

    def authenticate_request(self):
        print("main.authenticate_request")
        return Auth(self.db).authenticate_token(
            self.request_params[USERNAME],
            self.request_params[DEVICE_ID],
            self.request_params[TOKEN]
        )

    def authenticate_token(self):
        print("main.authenticate_token")
        if not self.request_params[STATUS]:
            result = False
            msg = E400
            print(msg)
            print()
            print(f"auther == {self.authenticate_request()}")
        elif not self.authenticate_request():
            result = False
            msg = E401
            print(msg)
        else:
            result = True
            msg = S200
            print(msg)
        return self.response_builder(
            result=result,
            msg=msg
        )

    def authenticate_login(self):
        print("main.authenticate_login")
        token = None
        auth = Auth(self.db)
        if not self.request_params[STATUS]:
            result = False
            msg = E400
            print(msg)
        elif not self.request_params[USERNAME]:
            result = False
            msg = E402
            print(msg)
        elif not self.request_params[PASSWORD]:
            result = False
            msg = E403
            print(msg)
        elif not self.request_params[DEVICE_ID]:
            result = False
            msg = E408
            print(msg)
        else:
            username = self.request_params[USERNAME]
            password = self.request_params[PASSWORD]
            device_id = self.request_params[DEVICE_ID]
            token = auth.authenticate_login(username, password, device_id)
            result = True if token else False
            msg = S201 if result else E404
            print(msg)
        return self.response_builder(
            result=result,
            token=token,
            msg=msg
        )

    def get_user_data(self):
        print("main.get_user_data")
        data = None
        if not self.request_params[STATUS]:
            result = False
            msg = E400
            print(msg)
        elif not self.authenticate_request():
            result = False
            msg = E401
            print(msg)
        elif not self.request_params[USERNAME]:
            result = False
            msg = E402
            print(msg)
        else:
            username = self.request_params[USERNAME]
            user_groups = Groups(self.db).get_user_groups(username)
            user_tasks = Tasks(self.db).get_user_tasks(username)
            user_friends = Friends(self.db).get_user_friends(username)

            data = {
                GROUPS: user_groups,
                TASKS: user_tasks,
                FRIENDS: user_friends
            }
            result = True
            msg = S200
            print(msg)
        return self.response_builder(
            result=result,
            msg=msg,
            data=data
        )

    def register_user(self):
        print("main.register_user")
        auth = Auth(self.db)
        token = None
        if not self.request_params[STATUS]:
            result = False
            msg = E400
            print(msg)
        elif not self.request_params[USERNAME]:
            result = False
            msg = E402
            print(msg)
        elif not self.request_params[MOBILE]:
            result = False
            msg = E405
            print(msg)
        elif not self.request_params[DEVICE_ID]:
            result = False
            msg = E408
            print(msg)
        elif not self.request_params[PASSWORD]:
            result = False
            msg = E403
            print(msg)
        else:
            mobile = self.request_params[MOBILE]
            if auth.validate_user_exists(mobile):
                result = False
                msg = E406
                print(msg)
            else:
                username = self.request_params[USERNAME]
                password = self.request_params[PASSWORD]
                device_id = self.request_params[DEVICE_ID]
                result = Auth(self.db).register_user(username, mobile, password)
                msg = S203 if result else E407
                if result:
                    token = auth.create_user_token(username, device_id)
                    result = Groups(self.db).register_personal_group(username)
                    print(msg)
        return self.response_builder(
            result=result,
            token=token,
            msg=msg
        )

    def register_group(self):
        print("main.register_group")
        if not self.request_params[STATUS]:
            result = False
            msg = E400
            print(msg)
        elif not self.authenticate_request():
            result = False
            msg = E401
            print(msg)
        elif not self.request_params[GROUP]:
            result = False
            msg = E411
            print(msg)
        else:
            user_group = self.request_params[GROUP]
            result = Groups(self.db).get_user_groups(user_group)
            msg = S203 if result else E412
            print(msg)
        return self.response_builder(
            result=result,
            msg=msg
        )

    def register_task(self):
        print("main.register_task")
        pass

    def delete_user(self):
        print("main.delete_user")
        pass

    def delete_group(self):
        print("main.delete_group")
        pass

    def delete_task(self):
        print("main.delete_task")
        pass

    def logout_user(self):
        print("main.logout_user")
        if not self.request_params[STATUS]:
            result = False
            msg = E400
        elif not self.authenticate_request():
            result = False
            msg = E401
        elif not self.request_params[USERNAME]:
            result = False
            msg = E402
        elif not self.request_params[DEVICE_ID]:
            result = False
            msg = E408
        elif not self.request_params[TOKEN]:
            result = False
            msg = E409
        else:
            username = self.request_params[USERNAME]
            device_id = self.request_params[DEVICE_ID]
            token = self.request_params[TOKEN]
            result = Auth(self.db).logout_user(username, device_id, token)
            msg = S204 if result else E410
        return self.response_builder(
            result=result,
            msg=msg
        )










