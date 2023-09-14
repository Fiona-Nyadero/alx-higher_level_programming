#!/usr/bin/python3
"""Fx creates an Object from json"""
import json


def load_from_json_file(filename):
    """Creates an object from JSONfile"""
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
