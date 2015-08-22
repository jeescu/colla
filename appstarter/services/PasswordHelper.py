__author__ = 'john'
import base64

class PasswordHelper(object):

    def __init__(self):
        pass

    def encode(self, string):
        return base64.encodestring(string)

    def decode(self, code):
        return base64.decodestring(code)