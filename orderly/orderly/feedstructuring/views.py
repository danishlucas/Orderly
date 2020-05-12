from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("This is the feed structuring app")

from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Notification

# Subclass RSS 2.0 feed
class LatestEntriesFeed(Feed):
    # Standard RSS fields
    title = "Orderly"
    link = "/feed/rss"
    description = "Chore schedule updates"

    # Get most recent 5 notifications
    def items(self):
        return Notification.objects.order_by('-timestamp')[:5]

    # Get info for notification
    def item_title(self, item):
        return item.uuid

    def item_description(self, item):
        return item.action