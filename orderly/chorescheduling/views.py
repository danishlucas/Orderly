from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person
import json, datetime

# bugs 
# - won't allow you to delete person if they are assigned to chore, won't allow to delete household
# - works if num_chores >= num_people, but consider case where num_people > num_chores
# - varying chore frequency

# parameters: username (email), first name, last name, password
# preconditions: user with same username does not already exist 
# postconditions: user created, will return "User already exists" error message if user already exists
# use case: signing up for an account
def create_user(request):
  data = json.load(request)
  PERSON_USERNAME = data['username']
  PERSON_FIRSTNAME = data['firstname']
  PERSON_LASTNAME = data['lastname']
  PERSON_PASSWORD = data['password']
  # --------------------------------
  # PERSON_USERNAME = "ben@gmail.com"
  # PERSON_FIRSTNAME = "Ben"
  # PERSON_LASTNAME = "Ten"
  # PERSON_PASSWORD = "benten"

  # checking is user already in database
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
  data = json.load(request)
  PERSON_USERNAME = data['username']
  PERSON_PASSWORD = data['password']
  # --------------------------------
  # PERSON_USERNAME = "ben@gmail.com"
  # PERSON_PASSWORD = "benten"

  user = authenticate(username=PERSON_USERNAME, password=PERSON_PASSWORD)

  # checking if username/password combo valid
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
def get_active_user(request):
  current_user = request.user 
  
  # checking to see if anyone actually logged in
  if current_user.username == "":
    data = {
      'person_id' : "-",
      'username' : "-", 
      'error_message' : "No one logged in"
    }
    return JsonResponse(data)
  else: 
    current_person = Person.objects.get(name=current_user.username)
    data = {
      'person_id' : current_person.pid,
      'username' : current_person.name, 
      'error_message' : "-"
    }
    return JsonResponse(data)

# parameters: username
# preconditions: - 
# postconditions: returns error message "User does not exist" if user doesn't exist
# use case: get information about specified user
def get_user_details(request):
  data = json.load(request)
  USERNAME = data['username']
  # --------------------------------
  # USERNAME = "ben@gmail.com"
  
  # checking to see if user exists
  if not Person.objects.filter(name=USERNAME).exists(): 
    data = {
      'firstname' : "-",
      'lastname' : "-",
      'username' : "-", 
      'person_id' : "-",
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "User does not exist"
    }
    return JsonResponse(data)
  # checking to see if user has no houshold attached to them
  elif Person.objects.get(name=USERNAME).linked_household is None:
    current_person = Person.objects.get(name=USERNAME)
    current_user = User.objects.get(username=USERNAME)
    data = {
      'firstname' : current_user.first_name,
      'lastname' : current_user.last_name,
      'username' : current_user.username, 
      'person_id' : current_person.pid,
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "-"
    }
    return JsonResponse(data)
  # user exists, has household attached
  else:
    current_person = Person.objects.get(name=USERNAME)
    current_user = User.objects.get(username=USERNAME)
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
# use case: get schedule and schedule details associated with household
def get_full_schedule(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  # --------------------------------
  # HOUSEHOLD_ID = 1

  # checking to see if schedule exists for given household
  if not Schedule.objects.filter(linked_household_id=HOUSEHOLD_ID).exists():
    data = {
      'schedule_id' : "-",
      'start_date' : "-",
      'num_weeks' : "-", 
      'household_id' : "-",
      'weeks' : [],
      'error_message' : "Schedule for household doesn't exist"
    }
    return JsonResponse(data)
  else:
    schedule = Schedule.objects.get(linked_household_id=HOUSEHOLD_ID)

    week_list = []
    for x in range(0, schedule.num_weeks):
      week = Week.objects.get(week_num=x, linked_schedule_id=schedule.sid)
      week_list.append(week)

    weeks = []
    counter = 0
    for week in week_list: 
      week_num = "week" + str(counter)
      json_chores = {week_num : []}
      chores_for_week = Chore.objects.filter(linked_week=week)

      for chore in chores_for_week:
        json_chores[week_num].append({"chore_name" : chore.chore_info.name, "chore_description" :  chore.chore_info.description, "assigned_to" : chore.assigned_to.name, "date" : chore.date})

      counter += 1
      weeks.append(json_chores)

    data = {
      'schedule_id' : schedule.sid,
      'start_date' : schedule.start_date,
      'num_weeks' : schedule.num_weeks, 
      'household_id' : schedule.linked_household_id,
      'weeks' : weeks,
      'error_message' : "-"
    }
    return JsonResponse(data)

# parameters: household id, week num (zero-based indexing)
# preconditions: schedule for household exists
# postconditions: will return error message if no schedule generated or week does not exist
# use case: get schedule for the week
def get_week_schedule(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  WEEK_NUM = data['week_num']
  # --------------------------------
  # HOUSEHOLD_ID = 1
  # WEEK_NUM = 7

  # checking to see if schedule exists for given household
  if not Schedule.objects.filter(linked_household_id=HOUSEHOLD_ID).exists():
    data = {
      'schedule_id' : "-",
      'start_date' : "-",
      'num_weeks' : "-", 
      'household_id' : "-",
      'week' : "-",
      'error_message' : "Schedule for household doesn't exist"
    }
    return JsonResponse(data)
  else:
    schedule = Schedule.objects.get(linked_household_id=HOUSEHOLD_ID)

    if not Week.objects.filter(week_num=WEEK_NUM, linked_schedule_id=schedule.sid).exists():
      data = {
        'schedule_id' : "-",
        'start_date' : "-",
        'num_weeks' : "-", 
        'household_id' : "-",
        'week' : "-",
        'error_message' : "No week exists, need to pass in a lower week"
      }
      return JsonResponse(data)

    week = Week.objects.get(week_num=WEEK_NUM, linked_schedule_id=schedule.sid)
    chores = []
    chores_for_week = Chore.objects.filter(linked_week=week)

    for chore in chores_for_week:
      chores.append({"chore_name" : chore.chore_info.name, "chore_description" :  chore.chore_info.description, "assigned_to" : chore.assigned_to.name, "date" : chore.date})

    data = {
      'schedule_id' : schedule.sid,
      'start_date' : schedule.start_date,
      'num_weeks' : schedule.num_weeks, 
      'household_id' : schedule.linked_household_id,
      'week' : chores,
      'error_message' : "-"
    }
    return JsonResponse(data)


# parameters: household name
# preconditions: user logged in and not linked to another household
# postconditions: household created and currently logged in user set to admin of household, will return 
#                 error messages if no user logged in or user already linked to another household
# use case: after admin creates account, would have the option to create a household
def create_household(request):
  data = json.load(request)
  HOUSEHOLD_NAME = data['name']
  # --------------------------------
  # HOUSEHOLD_NAME = "The Crib"

  current_user = request.user

  # checking to see if user logged in
  if current_user.username == "":
    data = {
      'household_id' : "-",
      'household_name' : "-",
      'household_admin' : "-",
      'error_message' : "User needs to be logged in to create household"
    }
    return JsonResponse(data)
  # checking to ensure that user not linked to another household already
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

# parameters: household ID
# preconditions: household created
# postconditions: 
# use case: when accessing all the household users
def get_household_users(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  # --------------------------------
  # HOUSEHOLD_ID = 1

  if not Household.objects.filter(hid=HOUSEHOLD_ID).exists():
    data = {"people" : []}
    return JsonResponse(data)
  else: 
    data = {"people" : []}
    target_people = Person.objects.filter(linked_household_id=HOUSEHOLD_ID)
    household_admin = Household.objects.get(hid=HOUSEHOLD_ID).admin
    for person in target_people: 
      user = User.objects.get(username=person.name)
      is_admin = person.name == household_admin.name
      person_data = {"pid" : person.pid, "username" : person.name, "first_name" : user.first_name, "last_name" : user.last_name, "is_admin" : is_admin}
      data["people"].append(person_data)
    return JsonResponse(data)


# parameters: household ID, list of usernames
# preconditions: household created, user to be added to household created
# postconditions: user added to househould
# use case: initial set-up OR adding someone to household through options
def add_household_users(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  PERSON_USERNAMES = data['usernames']
  # --------------------------------
  # HOUSEHOLD_ID = 1
  # PERSON_USERNAMES = ["ariana@gmail.com", "caleb@gmail.com"]
  
  data = {"household_id" : HOUSEHOLD_ID, "people_added" : []}

  for person_username in PERSON_USERNAMES:
    person = Person.objects.get(name=person_username)
    person.linked_household_id = HOUSEHOLD_ID
    person.save()
    data["people_added"].append(person_username)

  return JsonResponse(data)

# parameters: household ID, list of usernames
# preconditions: household created, user to be added to household created
# postconditions: users removed from househould
# use case: modifying list of users
def remove_household_users(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  PERSON_USERNAMES = data['usernames']
  # --------------------------------
  # HOUSEHOLD_ID = 1
  # PERSON_USERNAMES = ["ariana@gmail.com", "caleb@gmail.com"]
  
  data = {"household_id" : HOUSEHOLD_ID, "people_removed" : []}

  for person_username in PERSON_USERNAMES:
    person = Person.objects.get(name=person_username)
    person.linked_household = None
    person.save()
    data["people_removed"].append(person_username)

  return JsonResponse(data)

# parameters: household ID, list of chores/descriptions
# preconditions: household created
# postconditions: choreinfos created and linked to that househould, prevents chores with same name from being created for a given household
# use case: initial set-up OR when resetting chore schedule through options
def add_household_chores(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  CHORE_NAMES = data['names']
  CHORE_DESCRIPTIONS = data['descriptions']
  # --------------------------------
  # HOUSEHOLD_ID = 1
  # CHORE_NAMES = ["Kitchen", "Dining Room", "Living Room"]
  # CHORE_DESCRIPTIONS = ["description1", "description2", "description3"]

  data = {"household_id" : HOUSEHOLD_ID, "added_chore_names" : [], "added_chore_descriptions" : []}
  
  for x in range(0, len(CHORE_NAMES)):
    if not ChoreInfo.objects.filter(name=CHORE_NAMES[x], linked_household_id=HOUSEHOLD_ID).exists():
      chore_info = ChoreInfo(name=CHORE_NAMES[x], description=CHORE_DESCRIPTIONS[x], linked_household_id=HOUSEHOLD_ID)
      chore_info.save()
      data["added_chore_names"].append(CHORE_NAMES[x])
      data["added_chore_descriptions"].append(CHORE_DESCRIPTIONS[x])
    
  return JsonResponse(data)

# parameters: household ID, list of chores/descriptions
# preconditions: household created, choreinfos exist
# postconditions: choreinfos removed
# use case: modifying chore list
def remove_household_chores(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  CHORE_NAMES = data['names']
  CHORE_DESCRIPTIONS = data['descriptions']
  # --------------------------------
  # HOUSEHOLD_ID = 2
  # CHORE_NAMES = ["Living Room", "Dining Room", "Kitchen"]

  data = {"household_id" : HOUSEHOLD_ID, "removed_chore_names" : []}
  
  for x in range(0, len(CHORE_NAMES)): 
    choreinfo = ChoreInfo.objects.get(linked_household_id=HOUSEHOLD_ID, name=CHORE_NAMES[x])
    data["removed_chore_names"].append(choreinfo.name)
    choreinfo.delete()
    
  return JsonResponse(data)

# parameters: household id, number of weeks for schedule, start date month, start date day, start date year
# preconditions: household created and choreinfos/people been defined 
# postcondition: within schedule, weeks generated .... within weeks, list of chores assigned to people
# use case: initial set-up (after defining choreinfos/people) OR when resetting chore schedule through options
def generate_schedule(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  SCHEDULE_NUM_WEEKS = data['num_weeks']
  STARTDATE_MONTH = data['month']
  STARTDATE_DAY = data['day']
  STARTDATE_YEAR = data['year']
  # --------------------------------
  # HOUSEHOLD_ID = 1 
  # SCHEDULE_NUM_WEEKS = 5
  # STARTDATE_MONTH = 10
  # STARTDATE_DAY = 20
  # STARTDATE_YEAR = 2020

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
      json_chore_list[week_num].append({"chore_name" : chore_infos[x].name, "chore_description" : chore_infos[x].description, "assigned_to" : persons[(x + first_person) % num_people].name, "date" : current_date})

    first_person += 1
    current_date += datetime.timedelta(days=7)
    json_week_list["weeks"].append(json_chore_list)

  return JsonResponse(json_week_list)