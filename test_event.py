import event_types
import parser
import unittest


'''
Use examples 
'''
x = event_types.BaseRequest('test')


y = event_types.LoginRequest('test2')

pr = parser.EventParser()

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


if __name__ == '__main__':
    unittest.main()
