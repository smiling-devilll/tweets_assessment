import json
import django
from assessment import tweets_proc
from assessment import text_emotion_assessment
from assessment.Message import Message
from assessment.message_wrapper import Message_wrapper


__author__ = 'Victoria'
import datetime


def assess(hash_tag):
    print(datetime.datetime.now())
    tweets = tweets_proc.get_tweets_by_hash_tag(hash_tag)
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(Message(tweet.text))
    wrapper = Message_wrapper(tweet_list)
    print(datetime.datetime.now())

    assessments = text_emotion_assessment.get_assessment(json.dumps(wrapper, default=Message_wrapper.json_default))
    for assessment in assessments:
        print("tweet: " + assessment.get("text") + " assessment: " + str(assessment.get("polarity")))
    print(datetime.datetime.now())

print(django.get_version())
# assess("penny dreadful")