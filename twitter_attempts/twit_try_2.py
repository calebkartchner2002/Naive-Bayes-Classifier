import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
# Twitter API credentials
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Authenticate with Twitter API v2 using Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_tweets(count=2):
    # Use a simple keyword to search for tweets
    query = 'news OR trending OR random OR happy -is:retweet'  # Exclude retweets
    tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=count)

    # Get the tweet text
    tweet_list = [tweet.text for tweet in tweets.data]
    
    return tweet_list

if __name__ == "__main__":
    tweets = get_tweets(2)
    for i, tweet in enumerate(tweets, 1):
        print(f"Tweet {i}: {tweet}\n")
