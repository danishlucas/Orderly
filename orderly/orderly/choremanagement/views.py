from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chorescheduling.models import Household, Schedule, Week, Chore, ChoreInfo, Person

# Create your views here.
def index(request):
  return HttpResponse("This is the chore management app")

# parameters: Chore ID, completed
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore completion status changed to completed
# use case: user wants to change completion status of a certain chore
# JSON format: 
#            'all_users_linked': true on success, false on failure
def change_chore_completion_status(request):
  # CHORE_ID = request.GET.get('cid', None)
  CHORE_ID = 20
  # COMPLETED = request.GET.get('completed', None)
  COMPLETED = True

  chore = Chore.objects.get(cid=CHORE_ID)
  chore.completed = COMPLETED
  chore.save()
  linked = True
  # output = "Changed completion status of " + chore_info.name + " to " + COMPLETED
  data = {
    'all_users_linked': linked
  }
  return JsonResponse(data)
  # return HttpResponse(output, content_type="text/plain")

# parameters: Chore ID, giver, reciever
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore becomes assigned to reciever on success
# use case: user trades chore to someone else
# JSON format: 
#            'all_users_linked': true on success, false on failure
def change_chore_assignment(request):
  # CHORE_ID = request.GET.get('cid', None)
  CHORE_ID = 20
  # GIVER_PERSON = request.GET.get('giver', None)
  GIVER_PERSON_ID = 3
  # RECIEVER_PERSON = request.GET.get('reciever', None)
  RECIEVER_PERSON_ID = 4

  giver = Person.objects.get(pid=GIVER_PERSON_ID)
  chore = Chore.objects.get(cid=CHORE_ID)
  chore_info = ChoreInfo.objects.get(ciid=chore.chore_info_id)
  linked = True
  if chore.assigned_to != GIVER_PERSON_ID:
    # output = "Person " + giver.name + " is not assigned to chore " + chore_info.name
    linked = False
    # return HttpResponse(output, content_type="text/plain")

  chore.assigned_to = RECIEVER_PERSON_ID
  reciever = Person.objects.get(pid=RECIEVER_PERSON_ID)
  chore.save()
  data = {
    'all_users_linked': linked
  }
  return JsonResponse(data)
  # output = "Chore " + chore_info.name + " is now assigned to " + reciever.name + " from " + giver.name
  # return HttpResponse(output, content_type="text/plain")

# parameters: Household ID
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: no database changes made
# use case: to display the chore schedule for a household
def view_household_chore_schedule(request):
  # HOUSEHOLD_ID = request.GET.get('hid', None)
  HOUSEHOLD_ID = 6
  household = Household.objects.get(hid=HOUSEHOLD_ID)
  schedule = Schedule.objects.get(sid=household.linked_schedule)

  # get all weeks for this schedule
  week_list = []
  for week in Week.objects.filter(linked_schedule=schedule.sid):
    week_list.append(week)

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

# parameters: Person ID
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: no database changes made
# use case: to display the chore schedule for a single person
#           Note: this  includes chores for a person regardless of completion status
# JSON format:
#   'pid': Person ID
#   'chore_list': list of chore IDs
def view_individual_chore_schedule(request):
  PERSON_ID = request.GET.get('pid', None)

  chore_list = []
  for chore in Chore.objects.filter(assigned_to=PERSON_ID):
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
#   'cid': Chore ID,
#   'ciid': Chore Info ID,
#   'name': Chore Info Name,
#   'description': Chore Info Description,
#   'assigned_to': pid of person this chore is assigned to,
#   'completed': True/False based on whether chore is completed,
#   'hid': house id of this chore
def get_chore_info(request):
  CHORE_ID = request.GET>get('cid', None)
  chore = Chore.objects.get(cid=CHORE_ID)
  chore_info = ChoreInfo.objects.get(ciid=chore.chore_info)
  data = {
    'cid': CHORE_ID,
    'ciid': chore_info.ciid,
    'name': chore_info.name,
    'description': chore_info.description,
    'assigned_to': chore.assigned_to,
    'completed': chore.completed,
    'hid': chore_info.linked_household
  }
  return JsonResponse(data)