from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person

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
  # PERSON_NAME = request.GET.get('name', None)
  PERSON_NAME = "Earnie"
  
  person = Person(name=PERSON_NAME)
  person.save()
  user_output = "User " + str(person.name) + " created"

  # data = {
  #   'user_created': User.objects.filter(name=PERSON_NAME).exists()
  # }
  # return JsonResponse(data)
  return HttpResponse(user_output, content_type="text/plain")

# parameters: -
# preconditions: - 
# postconditions: household created
# use case: after leader creates account, would have the option to create a household
def create_household(request):
  household = Household()
  household.save()
  household_output = "Household " + str(household.hid) + " created"

  # data = {
  #   'household_created': Household.objects.filter(hid=household.hid).exists()
  # }
  # return JsonResponse(data)
  return HttpResponse(household_output, content_type="text/plain")

# parameters: household ID, list of users
# preconditions: household created, user to be added to household created
# postconditions: user added to househould
# use case: initial set-up OR adding someone to household through options
def add_household_users(request):
  # HOUSEHOLD_ID = request.GET.get('hid', None)
  # PERSON_NAMES = request.GET.get('names', None)
  HOUSEHOLD_ID = 6
  PERSON_NAMES = ["Dorothy", "Earnie"]

  people_output = ""
  linked = True
  for person_name in PERSON_NAMES:
    person = Person.objects.get(name=person_name)
    person.linked_household_id = HOUSEHOLD_ID
    person.save()
    people_output += person.name + '\n'

    if Person.objects.get(name=person_name).linked_household_id != HOUSEHOLD_ID:
      linked = False
  people_output += '\n' + "Users added to household " + str(HOUSEHOLD_ID)

  # data = {
  #   'all_users_linked': linked
  # }
  # return JsonResponse(data)
  return HttpResponse(people_output, content_type="text/plain")

# parameters: household ID, list of chores/descriptions
# preconditions: household created
# postconditions: choreinfos created and linked to that househould
# use case: initial set-up OR when resetting chore schedule through options
def add_household_chores(request):
  # HOUSEHOLD_ID = request.GET.get('hid', None)
  # CHORE_NAMES = request.GET.get('names', None)
  # CHORE_DESCRIPTIONS = request.GET.get('descriptions', None)
  HOUSEHOLD_ID = 6
  CHORE_NAMES = ["chore 4", "chore 5", "chore 6"]
  CHORE_DESCRIPTIONS = ["description 4", "decription 5", "description 6"]
  
  chore_output = ""
  linked = True
  for x in range(0, len(CHORE_NAMES)): 
    chore_info = ChoreInfo(name=CHORE_NAMES[x], description=CHORE_DESCRIPTIONS[x], linked_household_id=HOUSEHOLD_ID)
    chore_info.save()
    chore_output += chore_info.name + " - " + chore_info.description + " created" + '\n'
    
    if ChoreInfo.objects.get(name=CHORE_NAMES[x]).linked_household_id != HOUSEHOLD_ID:
      linked = False
  chore_output += '\n' + "Chores linked with household " + str(HOUSEHOLD_ID)
  
  # data = {
  #   'all_users_linked': linked
  # }
  # return JsonResponse(data)
  return HttpResponse(chore_output, content_type="text/plain")

# parameters: household id, number of weeks for schedule
# preconditions: household created and choreinfos/people been defined 
# postcondition: within schedule, weeks generated .... within weeks, list of chores assigned to people
# use case: initial set-up (after defining choreinfos/people) OR when resetting chore schedule through options
def generate_schedule(request):
  HOUSEHOLD_ID = 6
  SCHEDULE_NUM_WEEKS = 6

  household = Household.objects.get(hid=HOUSEHOLD_ID)

  try: 
    existing_schedule = Schedule.objects.get(linked_household__hid=HOUSEHOLD_ID)
    existing_schedule.delete()
  except: 
    pass
  schedule = Schedule(num_weeks=SCHEDULE_NUM_WEEKS, linked_household_id=household.hid)
  schedule.save()

  persons = Person.objects.filter(linked_household__hid=HOUSEHOLD_ID)
  chore_infos = ChoreInfo.objects.filter(linked_household__hid=HOUSEHOLD_ID)

  week_list = []
  for x in range(0, schedule.num_weeks):
    week = Week(week_num=x, linked_schedule_id=schedule.sid)
    week.save()
    week_list.append(week)

  # creating chores for each week 
  first_person = 0
  num_people = len(persons)
  for week in week_list:
    for x in range(0, len(chore_infos)): 
      ciid = chore_infos[x].ciid
      wid = week.wid 
      pid = persons[(x + first_person) % num_people].pid 
      chore = Chore(chore_info_id=ciid, linked_week_id=wid, assigned_to_id=pid)
      chore.save()
    first_person += 1

  # formatting schedule 
  household_output = "Household: " + str(HOUSEHOLD_ID) + '\n'
  schedule_output = "Schedule: " + str(schedule.sid) + ", Linked Household = " + str(schedule.linked_household_id) + ", Number of Weeks = " + str(schedule.num_weeks) + '\n' + '\n'
  week_output = ""
  for week in week_list: 
    week_output += "Week: " + str(week.week_num) + ", " + "Linked Schedule = " + str(week.linked_schedule_id) + '\n'
    chore_list = Chore.objects.filter(linked_week_id=week.wid) 
    for chore in chore_list: 
      chore_info = ChoreInfo.objects.get(ciid=chore.chore_info_id)
      person = Person.objects.get(pid=chore.assigned_to_id)
      week_output += "   " + "id = " + str(chore.cid) + ", " + chore_info.name + " --- " + person.name + '\n' 
    week_output += '\n'
  return HttpResponse(household_output + schedule_output + week_output, content_type="text/plain")