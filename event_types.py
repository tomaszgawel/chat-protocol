import time

LOGIN_REQUEST = 'LOGIN_REQUEST'
BASE = 'BASE'
MESSAGE_REQUEST = 'MESSAGE_REQUEST'


class BaseRequest:

    def __init__(self, login):
        self.timestamp = time.time()
        self.login = login
        self.event_type = BASE

    def convert_to_string(self):
        attributes_string = ''

        for attribute, value in self.__dict__.items():
            attributes_string += str(attribute)+':'+str(value)+'$$'

        attributes_string_len = len(attributes_string)

        return_string = ''

        return_string += 'length:' + \
            str(attributes_string_len)+'$$'+attributes_string

        return return_string


class LoginRequest(BaseRequest):

    def __init__(self, login):
        BaseRequest.__init__(self, login)
        self.event_type = LOGIN_REQUEST


class MessageRequest(BaseRequest):

    def __init__(self, login, message):
        BaseRequest.__init__(self, login)
        self.event_type = MESSAGE_REQUEST
        self.message = message



