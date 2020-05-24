from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the feed structuring app")

def get_notification(request, id):
    return HttpResponse("Notification")


from django.contrib.syndication.views import Feed
from .models import Notification
from chorescheduling.models import Household
from django.urls import reverse

# Subclass RSS 2.0 feed
class LatestEntriesFeed(Feed):
    # Get household for feed
    def get_object(self, request, household_id):
        return Household.objects.get(hid=household_id)

    # Get most recent 5 notifications
    def items(self, obj):
        return Notification.objects.filter(household_id=obj).order_by('-timestamp')[:10]

    # Get info for notification item
    def item_title(self, item):
        return item.id

    # Get description of notification item
    def item_description(self, item):
        return item.__str__() + " on chore " + str(item.chore_id.cid)

    # link to specific notification
    def item_link(self, item):
        return reverse('notification', args=[item.id])

    # title of feed
    def title(self, obj):
        return "Feed for household %s" % obj.household_name

    # link to household for feed
    def link(self, obj):
        return '/feedstructuring/feed/' + str(obj.hid)

    # description of feed
    def description(self, obj):
        return "Updates for chores in household %s" % obj.household_name