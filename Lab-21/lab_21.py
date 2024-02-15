import os

import tweepy


# Fetch credentials for Twitter API securely
CUSTOMER_KEY = os.getenv('CUSTOMER_KEY', None)
CUSTOMER_SECRET = os.getenv('CUSTOMER_SECRET', None)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', None)
ACCESS_SECRET = os.getenv('ACCESS_SECRET', None)

# Authentication
auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create client
client = tweepy.API(auth)

# Load user timeline
username = 'VMware'

tweets = client.user_timeline(username, count=5, page=1, tweet_mode='extended')
for t in tweets:
    print('----------')
    print(t.created_at) #-> return with UTC
    print(t.full_text)
