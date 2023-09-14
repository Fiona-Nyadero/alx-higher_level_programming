#!/usr/bin/python3
"""Fx returns a JSON object(str)"""
import json


def from_json_string(my_str):
    """Return a JSON object(str)"""

    return json.loads(my_str)
