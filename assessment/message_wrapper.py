__author__ = 'Victoria'
from assessment import Message
import json

class Message_wrapper:
    data = []

    def __init__(self, tweet):
        if isinstance(tweet, Message.Message):
            self.data.append(tweet)
        elif isinstance(tweet, list):
            self.data = tweet
        else: None


    def json_default(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self, default=Message_wrapper.json_default)

