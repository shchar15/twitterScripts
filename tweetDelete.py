import tweepy

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

def delete_all_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Retrieve and delete tweets
    for tweet in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(tweet.id)

# Usage: Call the function to delete all tweets
delete_all_tweets()
