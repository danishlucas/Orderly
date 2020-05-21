from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person
import json, datetime

# bugs 
# - remove household users, remove household chores
# - view schedule, pass in week and household no (or get from logged in user)
# - won't allow you to delete person if they are assigned to chore, won't allow to delete household
# - works if num_chores >= num_people, but consider case where num_people > num_chores
# - varying chore frequency
# - PUSH TO GIT


# parameters: username (email), first name, last name, password
# preconditions: user with same username does not already exist 
# postconditions: user created, will return "User already exists" error message if user already exists
# use case: signing up for an account
def create_user(request):
  # data = json.load(request)
  # PERSON_USERNAME = data['username']
  # PERSON_FIRSTNAME = data['firstname']
  # PERSON_LASTNAME = data['lastname']
  # PERSON_PASSWORD = data['password']
  # --------------------------------
  PERSON_USERNAME = "ben@gmail.com"
  PERSON_FIRSTNAME = "Ben"
  PERSON_LASTNAME = "Ten"
  PERSON_PASSWORD = "benten"
  # -------------------------------
  # PERSON_USERNAME = "caleb@gmail.com"
  # PERSON_FIRSTNAME = "Caleb"
  # PERSON_LASTNAME = ""
  # PERSON_PASSWORD = "benten"

  if User.objects.filter(username=PERSON_USERNAME).exists():
    data = {
      'username' : "-", 
      'person_id' : "-",
      'error_message' : "User already exists"
    }
    return JsonResponse(data)
  else:
    created_user = User.objects.create_user(username=PERSON_USERNAME, email=PERSON_USERNAME, password=PERSON_PASSWORD, first_name=PERSON_FIRSTNAME, last_name=PERSON_LASTNAME)
    created_user.save()
    person = Person(name=PERSON_USERNAME, user=created_user)
    person.save()

    data = {
      'username' : PERSON_USERNAME, 
      'person_id' : Person.objects.get(name=PERSON_USERNAME).pid,
      'error_message' : "-"
    }
    return JsonResponse(data)

# parameters: username (email), password
# preconditions: - 
# postconditions: user logged in, will return "User credentials invalid" error message if login unsuccesful
# use case: logging in
def login_user(request):
  # data = json.load(request)
  # PERSON_USERNAME = data['username']
  # PERSON_PASSWORD = data['password']
  # --------------------------------
  # PERSON_USERNAME = "ben@gmail.com"
  # PERSON_PASSWORD = "benten"
  # --------------------------------
  PERSON_USERNAME = "ariana@gmail.com"
  PERSON_PASSWORD = "benten"

  user = authenticate(username=PERSON_USERNAME, password=PERSON_PASSWORD)

  if user is None:
    data = {
      'username' : "-", 
      'person_id' : "-",
      'error_message' : "User credentials invalid"
    }
    return JsonResponse(data)
  else:
    data = {
      'username' : PERSON_USERNAME, 
      'person_id' : Person.objects.get(name=PERSON_USERNAME).pid,
      'error_message' : "-"
    }
    login(request, user)
    return JsonResponse(data)

# parameters: -
# preconditions: - 
# postconditions: user logged out (session data for current request wiped out)
# use case: logging in
def logout_user(request):
  logout(request)
  return HttpResponse("Logged out!")

# parameters: -
# preconditions: - 
# postconditions: -
# use case: get information about logged in user
def get_user_details(request):
  current_user = request.user 
  if current_user.username == "":
    data = {
      'firstname' : "-",
      'lastname' : "-",
      'username' : "-", 
      'person_id' : "-",
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "No one logged in"
    }
    return JsonResponse(data)
  else:
    current_person = Person.objects.get(name=current_user.username)
    current_household = Household.objects.get(hid=current_person.linked_household_id)
    data = {
      'firstname' : current_user.first_name,
      'lastname' : current_user.last_name,
      'username' : current_user.username, 
      'person_id' : current_person.pid,
      'household_id' : current_person.linked_household_id,
      'household_name' : current_household.household_name,
      'household_admin' : current_household.admin.name,
      'error_message' : "-"
    }
    return JsonResponse(data)

# parameters: household id
# preconditions: schedule for household exists
# postconditions: will return error message "Schedule for household doesn't exist" if no schedule generated
# use case: get information about schedule associated with household
def get_schedule_details(request):
  # data = json.load(request)
  # HOUSEHOLD_ID = data['hid']
  # --------------------------------
  HOUSEHOLD_ID = 1

  if not Schedule.objects.filter(linked_household_id=HOUSEHOLD_ID).exists():
    data = {
      'schedule_id' : "-",
      'start_date' : "-",
      'num_weeks' : "-", 
      'household_id' : "-",
      'error_message' : "Schedule for household doesn't exist"
    }
    return JsonResponse(data)
  else:
    schedule = Schedule.objects.get(linked_household_id=HOUSEHOLD_ID)
    data = {
      'schedule_id' : schedule.sid,
      'start_date' : schedule.start_date,
      'num_weeks' : schedule.num_weeks, 
      'household_id' : schedule.linked_household_id,
      'error_message' : "-"
    }
    return JsonResponse(data)

# parameters: household name
# preconditions: user logged in and not linked to another household
# postconditions: household created and currently logged in user set to admin, will return error messages
#                 if no user logged in or user already linked to another household
# use case: after admin creates account, would have the option to create a household
def create_household(request):
  # data = json.load(request)
  # HOUSEHOLD_NAME = data['name']
  # --------------------------------
  HOUSEHOLD_NAME = "The Crib"

  current_user = request.user
  if current_user.username == "":
    data = {
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "User needs to be logged in to create household"
    }
    return JsonResponse(data)
  elif Person.objects.get(name=current_user.username).linked_household is not None:
    data = {
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "User already linked to another household"
    }
    return JsonResponse(data)
  else:
    current_person = Person.objects.get(name=current_user.username)
    household = Household(household_name=HOUSEHOLD_NAME, admin=current_person)
    household.save()
    current_person.linked_household = household
    current_person.save()
    data = {
      'household_id' : household.hid,
      'household_name' : household.household_name,
      'household_admin' : household.admin.name,
      'error_message' : "-"
    }
    return JsonResponse(data)

# ---------------

# parameters: household ID, list of usernames
# preconditions: household created, user to be added to household created
# postconditions: user added to househould
# use case: initial set-up OR adding someone to household through options
def add_household_users(request):
  # data = json.load(request)
  # HOUSEHOLD_ID = data['hid']
  # PERSON_USERNAMES = data['usernames']
  # --------------------------------
  HOUSEHOLD_ID = 1
  PERSON_USERNAMES = ["ariana@gmail.com", "caleb@gmail.com"]
  
  data = {"household_id" : HOUSEHOLD_ID, "people" : []}

  for person_username in PERSON_USERNAMES:
    person = Person.objects.get(name=person_username)
    person.linked_household_id = HOUSEHOLD_ID
    person.save()
    data["people"].append(person_username)

  return JsonResponse(data)

# parameters: household ID, list of chores/descriptions
# preconditions: household created
# postconditions: choreinfos created and linked to that househould
# use case: initial set-up OR when resetting chore schedule through options
def add_household_chores(request):
  # data = json.load(request)
  # HOUSEHOLD_ID = data['hid']
  # CHORE_NAMES = data['names']
  # CHORE_DESCRIPTIONS = data['descriptions']
  # --------------------------------
  HOUSEHOLD_ID = 1
  CHORE_NAMES = ["Kitchen", "Living Room", "Bathroom"]
  CHORE_DESCRIPTIONS = ["description1", "description2", "description3"]

  data = {"household_id" : HOUSEHOLD_ID, "chore_names" : [], "chore_descriptions" : []}
  
  for x in range(0, len(CHORE_NAMES)): 
    chore_info = ChoreInfo(name=CHORE_NAMES[x], description=CHORE_DESCRIPTIONS[x], linked_household_id=HOUSEHOLD_ID)
    chore_info.save()
    data["chore_names"].append(CHORE_NAMES[x])
    data["chore_descriptions"].append(CHORE_DESCRIPTIONS[x])
    
  return JsonResponse(data)

# -------------------------------------------------

# parameters: household id, number of weeks for schedule, start date month, start date day, start date year
# preconditions: household created and choreinfos/people been defined 
# postcondition: within schedule, weeks generated .... within weeks, list of chores assigned to people
# use case: initial set-up (after defining choreinfos/people) OR when resetting chore schedule through options
def generate_schedule(request):
  # data = json.load(request)
  # HOUSEHOLD_ID = data['hid']
  # SCHEDULE_NUM_WEEKS = data['num_weeks']
  HOUSEHOLD_ID = 1 
  SCHEDULE_NUM_WEEKS = 5
  STARTDATE_MONTH = 10
  STARTDATE_DAY = 20
  STARTDATE_YEAR = 2020

  household = Household.objects.get(hid=HOUSEHOLD_ID)

  # deletes existing schedule for household if exists
  try: 
    existing_schedule = Schedule.objects.get(linked_household__hid=HOUSEHOLD_ID)
    existing_schedule.delete()
  except: 
    pass
  current_date = datetime.date(STARTDATE_YEAR, STARTDATE_MONTH, STARTDATE_DAY)
  schedule = Schedule(num_weeks=SCHEDULE_NUM_WEEKS, linked_household_id=household.hid, start_date=current_date)
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
      chore = Chore(chore_info_id=ciid, linked_week_id=wid, assigned_to_id=pid, date=current_date)
      chore.save()
      json_chore_list[week_num].append({"chore_name" : chore_infos[x].name, "assigned_to" : persons[(x + first_person) % num_people].name, "date" : current_date})

    first_person += 1
    current_date += datetime.timedelta(days=7)
    json_week_list["weeks"].append(json_chore_list)

  return JsonResponse(json_week_list)