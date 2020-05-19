from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person
import json

# bugs 
# - won't allow you to delete person if they are assigned to chore, won't allow to delete household
# - integrate people fields into user
# - works if num_chores >= num_people, but consider case where num_people > num_chores
# - varying chore frequency

# parameters: person name
# preconditions: - 
# postconditions: user created
# use case: signing up for an account
def create_user(request):
  data = json.load(request)
  PERSON_NAME = data['name']
  
  person = Person(name=PERSON_NAME)
  person.save()

  data = {
    'user_created': Person.objects.filter(name=PERSON_NAME).exists()
  }
  return JsonResponse(data)

# parameters: -
# preconditions: - 
# postconditions: household created
# use case: after leader creates account, would have the option to create a household
def create_household(request):
  household = Household()
  household.save()

  data = {
    'household_id': Household.objects.get(hid=household.hid).hid
  }
  return JsonResponse(data)

# parameters: household ID, list of users
# preconditions: household created, user to be added to household created
# postconditions: user added to househould
# use case: initial set-up OR adding someone to household through options
def add_household_users(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  PERSON_NAMES = data['names']

  linked = True
  for person_name in PERSON_NAMES:
    person = Person.objects.get(name=person_name)
    person.linked_household_id = HOUSEHOLD_ID
    person.save()

    if Person.objects.get(name=person_name).linked_household_id != HOUSEHOLD_ID:
      linked = False

  data = {
    'all_users_linked': linked
  }
  return JsonResponse(data)

# parameters: household ID, list of chores/descriptions
# preconditions: household created
# postconditions: choreinfos created and linked to that househould
# use case: initial set-up OR when resetting chore schedule through options
def add_household_chores(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  CHORE_NAMES = data['names']
  CHORE_DESCRIPTIONS = data['descriptions']
  
  linked = True
  for x in range(0, len(CHORE_NAMES)): 
    chore_info = ChoreInfo(name=CHORE_NAMES[x], description=CHORE_DESCRIPTIONS[x], linked_household_id=HOUSEHOLD_ID)
    chore_info.save()
    
    if ChoreInfo.objects.get(name=CHORE_NAMES[x]).linked_household_id != HOUSEHOLD_ID:
      linked = False
  
  data = {
    'all_chores_linked': linked
  }
  return JsonResponse(data)

# parameters: household id, number of weeks for schedule
# preconditions: household created and choreinfos/people been defined 
# postcondition: within schedule, weeks generated .... within weeks, list of chores assigned to people
# use case: initial set-up (after defining choreinfos/people) OR when resetting chore schedule through options
def generate_schedule(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  SCHEDULE_NUM_WEEKS = data['num_weeks']

  household = Household.objects.get(hid=HOUSEHOLD_ID)

  try: 
    existing_schedule = Schedule.objects.get(linked_household__hid=HOUSEHOLD_ID)
    existing_schedule.delete()
  except: 
    pass
  schedule = Schedule(num_weeks=SCHEDULE_NUM_WEEKS, linked_household_id=household.hid)
  schedule.save()
  
  household.linked_schedule_id = schedule.sid
  household.save()
  
  persons = Person.objects.filter(linked_household__hid=HOUSEHOLD_ID)
  chore_infos = ChoreInfo.objects.filter(linked_household__hid=HOUSEHOLD_ID)

  week_list = []
  for x in range(0, schedule.num_weeks):
    week = Week(week_num=x, linked_schedule_id=schedule.sid)
    week.save()
    week_list.append(week)

  json_week_list = {"weeks" : []}

  # creating chores for each week 
  first_person = 0
  num_people = len(persons)
  for week in week_list:
    week_num = "week" + str(first_person)
    json_chore_list = {week_num : []}

    for x in range(0, len(chore_infos)): 
      ciid = chore_infos[x].ciid
      wid = week.wid 
      pid = persons[(x + first_person) % num_people].pid 
      chore = Chore(chore_info_id=ciid, linked_week_id=wid, assigned_to_id=pid)
      chore.save()
      json_chore_list[week_num].append({"chore_name" : chore_infos[x].name, "assigned_to" : persons[(x + first_person) % num_people].name})

    first_person += 1
    json_week_list["weeks"].append(json_chore_list)

  return JsonResponse(json_week_list)