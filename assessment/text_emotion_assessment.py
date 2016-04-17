__author__ = 'Victoria'

from assessment.message_wrapper import Message_wrapper
from assessment.Message import Message
from assessment.Polarity import Polarity
import json
import requests


def get_assessment(text="peaky blinders are wonderfuuuuul"):
    param = {"appid": "testova.vika@gmail.com"}
    r = requests.post("http://www.sentiment140.com/api/bulkClassifyJson", data=text, params=param)

    json_object = json.loads(r.text)
    return json_object.get("data")

# tweet_list = []
# tweet_list.append(Tweet("I love PB!"))
# tweet_list.append(Tweet("I hate mushrooms"))

# tweets = Tweet_wrapper(tweet_list)
# json_data = json.dumps(tweets, default=Tweet_wrapper.json_default)
# assessed_tweets = get_assessment(json_data)
# for tw in assessed_tweets:
#     print(tw.get("text"))
#     print(Polarity(tw.get("polarity")))