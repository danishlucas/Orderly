from django.shortcuts import render
from django.http import HttpResponse
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person

# bugs 
# - won't allow you to delete person if they are assigned to chore
# - people/chores not currently linked to a household

# preconditions: none 
# postconditions: household created
# use case: after leader creates account, would have the option to create a household
def create_household(request):
  household = Household()
  household.save()
  household_output = "Household " + str(household.hid) + " created"
  return HttpResponse(household_output)

# preconditions: none 
# postconditions: people created ... should find existing people and link to household CHANGE
# use case: after leader creates account, 
# def create_people(request):
#   PERSON_NAMES = ["person 1", "person 2", "person 3"] # PARAMETER TO PASS IN
#   for person_name in PERSON_NAMES:
#     person = Person(name=person_name) # NEED TO LINK TO HOUSEHOLD AS WELL
#     person.save()
#   return HttpResponse()

# preconditions: none 
# postconditions: household created
# use case: after leader creates account, 
# def create_chores(request):
#   CHORE_NAMES = ["chore 1", "chore 2", "chore 3"] # PARAMETER TO PASS IN
#   CHORE_DESCRIPTIONS = ["description 1", "decription 2", "description 3"] # PARAMETER TO PASS IN
#   for x in range(0, len(CHORE_NAMES)): 
#     chore_info = ChoreInfo(name=CHORE_NAMES[x], description=CHORE_DESCRIPTIONS[x])
#     chore_info.save()
#   return HttpResponse()

# parameters: household id, number of weeks for schedule
# preconditions: household created and choreinfos/people been defined 
# postcondition: within schedule, weeks generated .... within weeks, list of chores assigned to people
# use case: initial set-up (after defining choreinfos/people) OR when resetting chore schedule through options
def create_schedule(request):
  HOUSEHOLD_ID = 3
  SCHEDULE_NUM_WEEKS = 5

  household = Household.objects.get(hid=HOUSEHOLD_ID)

  try: 
    existing_schedule = Schedule.objects.get(linked_household__hid=HOUSEHOLD_ID)
    existing_schedule.delete()
  except: 
    pass
  schedule = Schedule(num_weeks=SCHEDULE_NUM_WEEKS, linked_household_id=household.hid)
  schedule.save()

  persons = Person.objects.all() # OBTAIN FROM HOUSEHOLD
  chore_infos = ChoreInfo.objects.all() # OBTAIN FROM HOUSEHOLD

  week_list = []
  for x in range(0, schedule.num_weeks):
    week = Week(week_num=x, linked_schedule_id=schedule.sid)
    week.save()
    week_list.append(week)

  # creating chores for each week 
  # SEEMS TO WORK IF NUM_CHORES >= NUM_PEOPLE, BUT RETHINK CASE WHERE NUM_PEOPLE > NUM_CHORES OR CHORES HAVE VARYING FREQUENCY
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