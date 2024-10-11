import tweepy
import os

# Load your bearer token from an environment variable or paste it directly
bearer_token = os.getenv('BEARER_TOKEN')  # Or set it directly, e.g. "YOUR_BEARER_TOKEN"
print(bearer_token)

# Initialize the client
client = tweepy.Client(bearer_token=bearer_token)

def search_tweets(query, max_results=2):
    # Use Twitter API to search tweets
    response = client.search_recent_tweets(query=query, 
                                           tweet_fields=['text', 'created_at', 'author_id'],
                                           max_results=max_results)
    
    # Output response data
    if response.data:
        for tweet in response.data:
            print(f"Tweet ID: {tweet.id}, Author ID: {tweet.author_id}, Text: {tweet.text}")
    else:
        print("No tweets found for the query.")

if __name__ == "__main__":
    search_query = "X developer"  # Set your search term here
    search_tweets(search_query)
