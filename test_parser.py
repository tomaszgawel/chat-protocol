import unittest
import event_types
import event_parser


class TestParserMethods(unittest.TestCase):
    x = event_types.BaseRequest('test')
    y = event_types.LoginRequest('test2')
    
    pr = event_parser.EventParser()

    def test_if_object_is_base_type(self):

        parsed_object = self.pr.parse_string_to_event(
            self.x.convert_to_string())

        self.assertEquals(parsed_object.event_type, event_types.BASE, msg=None)

    def test_if_object_is_login_request(self):
        parsed_object = self.pr.parse_string_to_event(self.y.convert_to_string())
        self.assertEquals(parsed_object.event_type, event_types.LOGIN_REQUEST, msg=None)

    def test_if_get_full_length_is_valid_login(self):
        self.assertEqual(21, event_parser.get_full_length("length:10$$login:user"))

    def test_if_get_full_length_is_valid_msg(self):
        self.assertEqual(113, event_parser.get_full_length("length:101$$event_type:msg$$login:user$"))
        
         
if __name__ == '__main__':
    unittest.main()
