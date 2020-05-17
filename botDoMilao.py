import twitter
from authentication import auth
import counter
from time import sleep


consumer_key, consumer_secret, access_token, access_token_secret = auth()

api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)

while counter.current_num_post() < 1001:
    sleep(5)

api.PostUpdate("Vou upar isso no meu github :)")
