import re
import tweepy
from celery import shared_task

from tweet.models import Tweet


@shared_task
def query_twitter_api():
    """Query Elon's twitter for references to keywords."""

    print("Query Initiating...")
    auth = tweepy.OAuthHandler(
        "Y8tOO4cljDTzxxSA18LwEFqVs",
        "PTH7ZgURuke4GzOhFXaIbwTRjlK1dSxaClBYALl5WriEm8Nhdo"
    )

    auth.set_access_token(
        "1140717029957222401-iL3Xj9yhQkJksyCOopMhI158dRDqpT",
        "2pxAMq7mk3UoZiSUa7sQAwscGjkAOw2gtL3MOPD6ASFLQ"
    )

    api = tweepy.API(auth)

    twitter_status = api.user_timeline(
        id="elonmusk", count=1, tweet_mode="extended"
    )[0]._json

    tweet_text = twitter_status["full_text"]

    if re.search(r'\bbitcoin\b', tweet_text):
        obj = {
            "twitter_handle": "elonmusk",
            "created_at": twitter_status["created_at"],
            "text": tweet_text
        }

        print("Tweet mentioning bitcoin found")
        tweet = Tweet(**obj)
        tweet.save()
    else:
        print("No tweet mentioning bitcoin found")
