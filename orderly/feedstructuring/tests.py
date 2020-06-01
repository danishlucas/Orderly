from django.test import TestCase
from .models import Notification
from chorescheduling.models import Chore, Household
import xml.etree.ElementTree as ET
from django.urls import reverse
from model_bakery import baker

# Create your tests here.
class RSSFeedTestCase(TestCase):

    def create_notification(self, action, household_id):
        chore = baker.make('chorescheduling.Chore')
        return Notification.objects.create(chore_id=chore, household_id=household_id, action=action)

    def test_feed_no_notifications(self):
        household = Household(household_name="test_household")
        household.save()

        response = self.client.get('/feedstructuring/feed/' + str(household.hid))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 0)

    def test_feed_one_notification(self):
        household = Household(household_name="test_household")
        household.save()

        self.create_notification(Notification.ACTIONS.COMPLETED.value, household)

        response = self.client.get('/feedstructuring/feed/' + str(household.hid))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 1)

    def test_feed_eleven_notifications(self):
        household = Household(household_name="test_household")
        household.save()

        for _ in range(11):
            self.create_notification(Notification.ACTIONS.COMPLETED.value, household)

        response = self.client.get('/feedstructuring/feed/' + str(household.hid))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 10)

    def test_feed_two_households(self):
        household1 = Household(household_name="test_household1")
        household1.save()

        household2 = Household(household_name="test_household2")
        household2.save()

        self.create_notification(Notification.ACTIONS.COMPLETED.value, household1)
        self.create_notification(Notification.ACTIONS.COMPLETED.value, household2)

        response = self.client.get('/feedstructuring/feed/' + str(household1.hid))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 1)