#!/usr/bin/python3

"""Fx writes an object to a textfile(uses JSON)"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a textfile using JSON rep"""

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
