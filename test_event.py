import event_types
import event_parser
import unittest


'''
Use examples 
'''
x = event_types.BaseRequest('test')


y = event_types.LoginRequest('test2')

pr = event_parser.EventParser()

lr = event_types.LoginResponse(event_types.CODE_ACCEPT)

lr_error = event_types.LoginResponse(event_types.CODE_ERROR)

ret_obj = pr.parse_string_to_event(y.convert_to_string())

print(ret_obj)


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


if __name__ == '__main__':
    unittest.main()
