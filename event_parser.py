import event_types
from collections import namedtuple


class EventParser:

    def parse_string_to_event(self, event_string):

        string_pairs = event_string.split('$$')

        object_props = {}
        for string_pair in string_pairs:

            if string_pair:

                key, value = string_pair.split(':')
                object_props[key] = value

        if object_props['event_type'] == event_types.BASE:
            parsed_object = namedtuple(
                "BaseEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.LOGIN_REQUEST:

            parsed_object = namedtuple(
                "LoginEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.MESSAGE_REQUEST:

            parsed_object = namedtuple(
                "MessageEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.ONLINE_REQUEST:

            parsed_object = namedtuple(
                "OnlineEvent", object_props.keys())(*object_props.values())

            return parsed_object

        elif object_props['event_type'] == event_types.LOGIN_RESPONSE:

            parsed_object = namedtuple(
                "LoginResponse", object_props.keys())(*object_props.values())

            return parsed_object

        return None


def get_full_length(data):
    length = int(data.split('$$')[0].split(":")[1])
    # adding extra values for "length:<value>$$"
    return length + 9 + len(str(length))
