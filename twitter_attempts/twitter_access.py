import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your own Twitter API credentials

api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Verify the authentication
try:
    user = api.verify_credentials()
    if user:
        print(f"Authentication successful! Logged in as: {user.screen_name} (ID: {user.id})")
    else:
        print("Authentication failed.")
except tweepy.TweepError as e:
    print(f"Error during authentication: {e}")


# Collect and print tweet details
def collect_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    for tweet in tweets:
        print(f"Tweet by @{tweet.user.screen_name} at {tweet.created_at}")
        print(f"Tweet ID: {tweet.id}")
        print(f"Text: {tweet.text}")
        print(f"Retweets: {tweet.retweet_count} | Likes: {tweet.favorite_count}")
        print("-" * 50)


collect_tweets('Python', 2)
