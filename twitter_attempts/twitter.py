import tweepy
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your own Twitter API credentials
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')  # You need to add the Bearer Token

"""# Authenticate to Twitter with API v2
client = tweepy.Client(bearer_token=bearer_token)

# Collect and print tweet details (using Twitter API v2)
def collect_tweets_v2(keyword, count=10):
    tweets = client.search_recent_tweets(query=keyword, max_results=count)
    for tweet in tweets.data:
        print(f"Tweet ID: {tweet.id}")
        print(f"Text: {tweet.text}")
        print("-" * 50)  # Divider for better readability

# Example: Collect 2 tweets containing the keyword 'Python'
collect_tweets_v2('Python', 2)

"""
#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 2

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))


