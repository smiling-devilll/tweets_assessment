__author__ = 'Victoria'

import json

class Message:
    text = ""

    def __init__(self, text):
        self.text = text

    def json_default(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self, default=Message.json_default)