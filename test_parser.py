import unittest
import event_types
import parser


class TestParserMethods(unittest.TestCase):
    x = event_types.BaseRequest('test')
    y = event_types.LoginRequest('test2')
    
    pr = parser.EventParser()

    def test_if_object_is_base_type(self):

        parsed_object = self.pr.parse_string_to_event(
            self.x.convert_to_string())

        self.assertEquals(parsed_object.event_type, event_types.BASE, msg=None)

    def test_if_object_is_login_request(self):
        parsed_object = self.pr.parse_string_to_event(self.y.convert_to_string())
        self.assertEquals(parsed_object.event_type, event_types.LOGIN_REQUEST, msg=None)
        
        
         
if __name__ == '__main__':
    unittest.main()
