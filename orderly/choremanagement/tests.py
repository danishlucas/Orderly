from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chorescheduling.models import Household, Schedule, Week, Chore, ChoreInfo, Person
from choremanagement.views import *
from django.contrib.auth.models import User
import json
from django.urls import reverse

class ChoreManagementTestCase(TestCase):
  
  def setUp(self):
    house = Household.objects.create(household_name="test_household")
    house_id = house.hid
    chore_1 = ChoreInfo.objects.create(name = "testChoreInfo", description = "testing", linked_household = house)
    chore_2 = ChoreInfo.objects.create(name = "testChoreInfo2", description = "testing2", linked_household = house)
    user_1 = User.objects.create_user(username="username", email="test", password="password", first_name="test", last_name="person")
    user_2 = User.objects.create_user(username="username2", email="test2", password="password2", first_name="test2", last_name="person2")
    person_1 = Person.objects.create(name = "testPerson", user = user_1, linked_household = house)
    person_2 = Person.objects.create(name = "testPerson2", user = user_2, linked_household = house)
    schedule_str = {
        'hid' : house_id,
        'num_weeks' : 1,
        'month' : 1,
        'day' : 10,
        'year' : 2020
    }
    schedule = Schedule.objects.create(num_weeks = 2, linked_household = house)
    week_1 = Week.objects.create(week_num = 1, linked_schedule = schedule)
    week_2 = Week.objects.create(week_num = 2, linked_schedule = schedule)
    test_chore_1 = Chore.objects.create(chore_info = chore_1, linked_week = week_1, assigned_to = person_1)
    test_chore_2 = Chore.objects.create(chore_info = chore_2, linked_week = week_1, assigned_to = person_2)
    test_chore_3 = Chore.objects.create(chore_info = chore_1, linked_week = week_2, assigned_to = person_2)
    test_chore_4 = Chore.objects.create(chore_info = chore_2, linked_week = week_2, assigned_to = person_1)

  def test_mark_chores_completed(self):
    chores = Chore.objects.all()
    for chore in chores:
      response_str = {'cid' : chore.cid,
                    'completed' : True 
                       }
      response = self.client.post(reverse('change_chore_completion_status'), 
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json(), {'all_users_linked' : True, 'new_chore_status' : True})
      tested_chore = Chore.objects.get(cid=chore.cid)
      self.assertEqual(tested_chore.completed, True)

  def test_mark_chore_uncompleted(self):
    chores = Chore.objects.all()
    for chore in chores:
      response_str = {'cid' : chore.cid,
                    'completed' : False 
                       }
      response = self.client.post(reverse('change_chore_completion_status'), 
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json(), {'all_users_linked' : True, 'new_chore_status' : False})
      tested_chore = Chore.objects.get(cid=chore.cid)
      self.assertEqual(tested_chore.completed, False)


  def test_trade_some_chores(self):
    chores = Chore.objects.all()
    for chore in chores:
      assigned_to = Person.objects.get(pid = chore.assigned_to.pid)
      other_person = None
      for person in Person.objects.all():
        if person.pid != assigned_to.pid:
          other_person = person.pid
      
      response_str = {'cid' : chore.cid,
                    'giver' : assigned_to.pid,
                    'reciever' : other_person 
                       }
      response = self.client.post(reverse('change_chore_assignment'),
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json(), {'all_users_linked' : True})
      tested_chore = Chore.objects.get(cid=chore.cid)
      self.assertEqual(other_person, tested_chore.assigned_to.pid)
  

  def test_fail_trade_chores(self):
    chores = Chore.objects.all()
    for chore in chores:
      assigned_to = Person.objects.get(pid = chore.assigned_to.pid)
      other_person = None
      for person in Person.objects.all():
        if person.pid != assigned_to.pid:
          other_person = person.pid
      response_str = {'cid' : chore.cid,
                    'giver' : other_person,
                    'reciever' : assigned_to.pid 
                       }
      response = self.client.post(reverse('change_chore_assignment'),
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json(), {'all_users_linked' : False})
      tested_chore = Chore.objects.get(cid=chore.cid)
      self.assertNotEqual(other_person, tested_chore.assigned_to.pid)

  def test_view_house_chore_schedule(self):
    households = Household.objects.all()
    for house in households:
      response_str = {'hid' : house.hid}
      response = self.client.post(reverse('view_household_chore_schedule'),
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(len(response.json()["weeks"]),2)
      self.assertEqual(len(response.json()["weeks"][0]["week0"]), 2)
      self.assertEqual(len(response.json()["weeks"][1]["week1"]), 2)

  def test_view_ind_chore_schedule(self):
    people = Person.objects.all()
    for person in people:
      response_str = {'pid' : person.pid}
      response = self.client.post(reverse('view_individual_chore_schedule'),
                                json.dumps(response_str), content_type = "application/json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json()["pid"], person.pid)
      self.assertEqual(len(response.json()["chore_list"]), 2)