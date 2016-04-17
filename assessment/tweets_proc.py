__author__ = 'Victoria'

import tweepy


def get_tweets_by_hash_tag(hash_tag="peaky_blinders"):
    # TweetsSentimentAnalysisTest
    # testova.vika@gmail.com
    consumer_key = "cIoqgL5YYPPmD4pAc4Swu9MeP"
    consumer_secret = "bWFUTmkvTburVhyC95MUgRqQdGyWNS8XUe3A8rnNFDW316ZKiE"
    access_key = "718523803308056577-QwGxva2FGubmnM2OVIKEJGryhgKibpR"
    access_secret = "negS0AHYXyBNMxDwPo2RmEKfrjXF17q1zXLKJmVxqW2mZ"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.search, q=hash_tag).items(10)
    return tweets
