from django.test import TestCase
from django.http import HttpResponse, JsonResponse
from chorescheduling.models import Household, Schedule, Week, Chore, ChoreInfo, Person
import xml.etree.ElementTree as ET
from django.urls import reverse
from model_bakery import baker

class ChoreManagementTestCase(TestCase):
  def setUp(self):
    Household.objects.create(hid=1)
    Person.objects.create(pid=1, name="Tom", linked_household=1)
    Person.objects.create(pid=2, name="Suzy", linked_household=1)
    Person.objects.create(pid=3, name="Fred", linked_household=1)
