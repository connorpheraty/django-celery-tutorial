import os
from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_example.settings")

app = Celery("django_celery_example")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    # Executes every 2 minutes
    "query-twitter-api": {
        "task": "tweet.tasks.query_twitter_api",
        "schedule": 120,
    },
}

