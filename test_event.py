import event_types
import event_parser
import unittest


'''
Use examples 
'''
x = event_types.BaseRequest('test')

y = event_types.LoginRequest('test2')

messageRequest = event_types.MessageRequest('test3', "Hello, it's a test")
onlineRequest = event_types.OnlineRequest()

onlineRequest.add_user("test")


pr = event_parser.EventParser()

lr = event_types.LoginResponse(event_types.CODE_ACCEPT)

lr_error = event_types.LoginResponse(event_types.CODE_ERROR)

ret_obj = pr.parse_string_to_event(y.convert_to_string())
message_obj = pr.parse_string_to_event(messageRequest.convert_to_string())


print(ret_obj)
print(messageRequest.convert_to_string())
print(message_obj)


class TestStringMethods(unittest.TestCase):

    x = event_types.BaseRequest('test')

    y = event_types.LoginRequest('test2')


    def test_login_1(self):
        string_x = x.convert_to_string()

        self.assertTrue('login:test' in string_x)

    def test_login_2(self):
        string_y = y.convert_to_string()

        self.assertTrue('login:test2' in string_y)

    def test_login_not_in(self):
        string_x = x.convert_to_string()

        self.assertTrue(not 'login:test2' in string_x)


    def test_code_in(self):
        self.assertTrue('code:dawaj mordo' in lr.convert_to_string())

    def test_code_not_in(self):
        self.assertTrue(not 'code:to jest kartofel' in lr_error.convert_to_string())

    def test_login_message_request(self):
        string_message_request = messageRequest.convert_to_string()
        self.assertTrue('login:test3' in string_message_request)

    def test_message_in_message_request(self):
        string_message_request = messageRequest.convert_to_string()
        self.assertTrue('message:Hello, it\'s a test' in string_message_request)

    def test_message_request_length_is_correct(self):
        string_message_request = messageRequest.convert_to_string()
        self.assertTrue('length:99' in string_message_request)

    def test_login_online_request(self):
        string_online_request = onlineRequest.convert_to_string()
        self.assertTrue('login:SERVER' in string_online_request)



if __name__ == '__main__':
    unittest.main()
