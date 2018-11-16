import json


class SmartLookup(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return key.title()
        return key


def to_lookup(dict):

    lookup  = SmartLookup()

    for key, values in dict.items():
        for value in values:
            lookup[value] = key


    return lookup
