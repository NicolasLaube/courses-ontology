"""Utility to load json from files"""

import json


def load_json(path):
    """To load a json file"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
