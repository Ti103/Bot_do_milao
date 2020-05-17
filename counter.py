import tweepy
from authentication import auth_tweepy
from time import sleep

auth = auth_tweepy()
difference = 2

api = tweepy.API(auth, wait_on_rate_limit=True)


def current_num_post():
    return len(list(tweepy.Cursor(api.user_timeline).items())) + 2
