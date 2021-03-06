from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chorescheduling.models import Household, Schedule, Week, Chore, ChoreInfo, Person
from feedstructuring.models import Notification
import json

# Create your views here.
def index(request):
  return HttpResponse("This is the chore management app")

# parameters: cid, completed
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore completion status changed to completed
# use case: user wants to change completion status of a certain chore
# JSON format: 
#            'all_users_linked': true on success, false on failure
#            'new_chore_status': boolean based on completed
def change_chore_completion_status(request):
  
  data = json.load(request)
  CHORE_ID = data['cid']
  # CHORE_ID = 20
  COMPLETED = data['completed']
  # COMPLETED = True
  chore = Chore.objects.get(cid=CHORE_ID)
  
  chore.completed = COMPLETED
  chore.save()
  linked = True
  
  notification = Notification(chore_id=chore, household_id=chore.chore_info.linked_household, action=Notification.ACTIONS.COMPLETED.value)
  notification.save()
  
  # output = "Changed completion status of " + chore_info.name + " to " + COMPLETED
  data = {
    'all_users_linked': linked,
    'new_chore_status': chore.completed
  }
  return JsonResponse(data)
  # return HttpResponse(output, content_type="text/plain")

# parameters: cid, giver, reciever
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore becomes assigned to reciever on success
# use case: user trades chore to someone else
# JSON format: 
#            'all_users_linked': true on success, false on failure
def change_chore_assignment(request):
  data = json.load(request)
  CHORE_ID = data['cid']
  GIVER_PERSON_ID = data['giver']
  RECIEVER_PERSON_ID = data['reciever']

  giver = Person.objects.get(pid=GIVER_PERSON_ID)
  chore = Chore.objects.get(cid=CHORE_ID)
  chore_info = ChoreInfo.objects.get(ciid=chore.chore_info_id)
  linked = True
  if chore.assigned_to.pid != GIVER_PERSON_ID:
    linked = False
  
  chore.assigned_to = Person.objects.get(pid=RECIEVER_PERSON_ID)
  reciever = Person.objects.get(pid=RECIEVER_PERSON_ID)
  chore.save()
  
  notification = Notification(chore_id=chore, household_id=chore.chore_info.linked_household, action=Notification.ACTIONS.CHANGED.value)
  notification.save()
  
  data = {
    'all_users_linked': linked
  }
  return JsonResponse(data)

# parameters: hid
# preconditions: household created and choreinfos/people been defined, chores have been assigned
# postconditions: no database changes made
# use case: to display the chore schedule for a household
def view_household_chore_schedule(request):
  data = json.load(request)
  HOUSEHOLD_ID = data['hid']
  schedule = Schedule.objects.get(linked_household__hid=HOUSEHOLD_ID)
  json_week_list = {"weeks" : []}

  # creating chores for each week 
  first_person = 0
  for week in Week.objects.filter(linked_schedule__sid=schedule.sid):
    week_num = "week" + str(first_person)
    json_chore_list = {week_num : []}
    chores = Chore.objects.filter(linked_week__wid=week.wid)
    for chore in chores: 
      chore_info = ChoreInfo.objects.get(ciid=chore.chore_info.ciid)
      assigned = Person.objects.get(pid=chore.assigned_to.pid)
      json_chore_list[week_num].append({"chore_name" : chore_info.name, "assigned_to" : assigned.name})

    first_person += 1
    json_week_list["weeks"].append(json_chore_list)

  return JsonResponse(json_week_list)

# parameters: Person ID
# preconditions: household created and choreinfos/people been defined, chores have been assigned
# postconditions: no database changes made
# use case: to display the chore schedule for a single person
#           Note: this  includes chores for a person regardless of completion status
# JSON format:
#   'pid': Person ID
#   'chore_list': list of chore IDs
def view_individual_chore_schedule(request):
  data = json.load(request)
  PERSON_ID = data['pid']

  chore_list = []
  for chore in Chore.objects.filter(assigned_to__pid=PERSON_ID):
    chore_list.append(chore.cid)

  data = {
    'pid': PERSON_ID,
    'chore_list': chore_list
  }
  return JsonResponse(data)

# parameters: Chore ID
# preconditions: household created and choreinfos/people been defined, chores have been assigned
# postconditions: no database changes made
# use case: to get the info for a specific chore
# JSON format:
# {
#   'cid': Chore ID,
#   'ciid': Chore Info ID,
#   'name': Chore Info Name,
#   'description': Chore Info Description,
#   'assigned_to': pid of person this chore is assigned to,
#   'completed': True/False based on whether chore is completed,
#   'hid': house id of this chore,
#   'week_num': week number for this chore
# }
# Note: more JSON fields for information about the chore can be added if needed
def get_chore_info(request):
  data = json.load(request)
  CHORE_ID = data['cid']
  chore = Chore.objects.get(cid=CHORE_ID)
  chore_info = ChoreInfo.objects.get(ciid=chore.chore_info.ciid)
  week = Week.objects.get(wid=chore.linked_week.wid)
  data = {
    'cid': CHORE_ID,
    'ciid': chore_info.ciid,
    'name': chore_info.name,
    'description': chore_info.description,
    'assigned_to': chore.assigned_to.pid,
    'completed': chore.completed,
    'hid': chore_info.linked_household.hid,
    'week_num': week.week_num
  }
  return JsonResponse(data)