from django.test import TestCase
from .models import Notification
from chorescheduling.models import ChoreInfo
import xml.etree.ElementTree as ET
from django.urls import reverse
from model_bakery import baker

# Create your tests here.
class RSSFeedTestCase(TestCase):
    chore_id = 0

    def create_notification(self, action):
        RSSFeedTestCase.chore_id += 1
        chore = baker.make('chorescheduling.Chore')
        return Notification.objects.create(chore_id=chore, action=action)

    def test_feed_no_notifications(self):
        response = self.client.get(reverse('feed'))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 0)

    def test_feed_one_notification(self):
        self.create_notification(Notification.ACTIONS.COMPLETED.value)

        response = self.client.get(reverse('feed'))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 1)

    def test_feed_six_notifications(self):
        for _ in range(5):
            self.create_notification(Notification.ACTIONS.COMPLETED.value)

        response = self.client.get(reverse('feed'))
        responseXml = ET.fromstring(response.content)
        items = responseXml[0].findall('item')

        self.assertEqual(len(items), 5)