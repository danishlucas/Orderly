from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the feed structuring app")

def get_notification(request, uuid):
    return HttpResponse("Notification")


from django.contrib.syndication.views import Feed
from .models import Notification
from django.urls import reverse

# Subclass RSS 2.0 feed
class LatestEntriesFeed(Feed):
    # Standard RSS fields
    title = "Orderly"
    link = "/feed/rss"
    description = "Chore schedule updates"

    # Get most recent 5 notifications
    def items(self):
        return Notification.objects.order_by('-timestamp')[:5]

    # Get info for notification item
    def item_title(self, item):
        return item.uuid

    # Get description of notification item
    def item_description(self, item):
        return item.__str__() + " on chore " + str(item.chore_id.ciid)

    def item_link(self, item):
        return reverse('notification', args=[item.uuid])