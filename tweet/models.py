from django.db import models


class Tweet(models.Model):

    # Add more fields with any additional metadata
    # from the twitter API you would like to track
    id = models.AutoField(primary_key=True)
    twitter_handle = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.twitter_handle
