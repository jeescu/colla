__author__ = 'john'

import json

class JsonResponseSerializer(object):

    def __init__(self):
        pass

    def to_json(self, object):
        return json.dumps(object, default=lambda o: o.__dict__, sort_keys=True, indent=4)