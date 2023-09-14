#!/usr/bin/python3
"""Fx returns the JSONrep of a str object"""

import json


def to_json_string(my_obj):
    """returns the JSON rep of a (str) object"""

    return json.dumps(my_obj)
