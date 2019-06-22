import event_types
from collections import namedtuple
from exceptions import ParsingProtocolException, ClientSocketInterruption

class EventParser:

    def parse_string_to_event(self, event_string):

        message = ''

        if not event_string:
            raise ClientSocketInterruption

        message_index_start = event_string.find("message:")

        if message_index_start == -1:
            object_props = self.split_string(event_string)

        else:
            message = str(event_string)[message_index_start + 8:-2]
            event_string = self.replace_from_index_to_index(event_string, "a", message_index_start + 8, len(event_string))
            print(event_string)
            object_props = self.split_string(event_string)

        if not 'event_type' in object_props:
            raise ParsingProtocolException

        if not 'login' in object_props:
            raise ParsingProtocolException

        if object_props['event_type'] == event_types.BASE:
            parsed_object = namedtuple(
                "BaseEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.LOGIN_REQUEST:

            parsed_object = namedtuple(
                "LoginEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.MESSAGE_REQUEST:
            object_props['message'] = message
            parsed_object = namedtuple(
                "MessageEvent", object_props.keys())(*object_props.values())
            print(parsed_object)
            return parsed_object

        elif object_props['event_type'] == event_types.ONLINE_REQUEST:

            parsed_object = namedtuple(
                "OnlineEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.LOGIN_RESPONSE:

            parsed_object = namedtuple(
                "LoginResponse", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.LOGOUT_REQUEST:

            parsed_object = namedtuple(
                "LogoutRequest", object_props.keys())(*object_props.values())

            return parsed_object


        raise ParsingProtocolException

    def replace_from_index_to_index(self, string, replace_to, index_start, index_end):
        return string[0:index_start] + replace_to + string[index_end + 1:]

    def split_string(self, event_string):
        try:
            object_props = {}
            string_pairs = event_string.split('$$')
            for string_pair in string_pairs:

                if string_pair:
                    key, value = string_pair.split(':')
                    object_props[key] = value

            return object_props

        except Exception as e:
            raise ParsingProtocolException

def get_full_length(data):
    length = int(data.split('$$')[0].split(":")[1])
    # adding extra values for "length:<value>$$"
    return length + 9 + len(str(length))