import tweepy

def auth():
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    access_token = "access_token"
    access_token_secret = "access_token_secret"

    return consumer_key, consumer_secret, access_token, access_token_secret

def auth_tweepy():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth
