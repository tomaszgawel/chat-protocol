import time
from datetime import datetime

LOGIN_REQUEST = 'LOGIN_REQUEST'
BASE = 'BASE'
MESSAGE_REQUEST = 'MESSAGE_REQUEST'
ONLINE_REQUEST = 'ONLINE_REQUEST'
LOGIN_RESPONSE = 'LOGIN_RESPONSE'
LOGOUT_REQUEST = 'LOGOUT_REQUEST'

CODE_ACCEPT = "dawaj mordo"
CODE_REJECT = "to jest kartofel"
CODE_ERROR = "Mateuszu nie kombinuj"


class BaseRequest:

    def __init__(self, login):
        self.timestamp = time.time()
        self.login = login
        self.event_type = BASE

    def convert_to_string(self):
        attributes_string = ''

        for attribute, value in self.__dict__.items():
            attributes_string += str(attribute) + ':' + str(value) + '$$'

        attributes_string_len = len(attributes_string)

        return_string = ''

        return_string += 'length:' + \
                         str(attributes_string_len) + '$$' + attributes_string

        return return_string

    def timestamp_to_datetime(self):
        return datetime.fromtimestamp(self.timestamp)


class LoginRequest(BaseRequest):

    def __init__(self, login):
        BaseRequest.__init__(self, login)
        self.event_type = LOGIN_REQUEST


class MessageRequest(BaseRequest):

    def __init__(self, login, message):
        BaseRequest.__init__(self, login)
        self.event_type = MESSAGE_REQUEST
        self.message = message


class OnlineRequest(BaseRequest):
    def __init__(self):
        BaseRequest.__init__(self, "SERVER")
        self.event_type = ONLINE_REQUEST
        self.online_users = []

    def consume_list(self, user_list):
        self.online_users = user_list

    def add_user(self, username):
        self.online_users.append(username)

    def new_online_users_list(self, online_users):
        self.online_users = online_users


class LoginResponse(BaseRequest):
    def __init__(self, code):
        BaseRequest.__init__(self, "SERVER")
        self.event_type = LOGIN_RESPONSE
        self.code = code


class LogoutRequest(BaseRequest):
    def __init__(self, login, is_logged_out):
        BaseRequest.__init__(self, login)
        self.event_type = LOGOUT_REQUEST
        self.is_logged_out = is_logged_out
