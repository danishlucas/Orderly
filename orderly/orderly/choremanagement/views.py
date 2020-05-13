from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chorescheduling.models import Household, Schedule, Week, Chore, ChoreInfo, Person
from feedstructuring.models import Notification

# Create your views here.
def index(request):
  return HttpResponse("This is the chore management app")

# parameters: Chore ID, completed
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore completion status changed to completed
# use case: user wants to change completion status of a certain chore
def change_chore_completion_status(request):
  # CHORE_ID = request.GET.get('cid', None)
  CHORE_ID = 20
  # COMPLETED = request.GET.get('completed', None)
  COMPLETED = True

  chore = Chore.objects.get(cid=CHORE_ID)
  chore_info = ChoreInfo.objects.get(ciid=chore.chore_info_id)
  chore_info.completed = COMPLETED
  chore_info.save()

  notification = Notification(chore_info=chore.chore_info_id, action=Notification.ACTIONS.COMPLETED.value)
  notification.save()

  output = "Changed completion status of " + chore_info.name + " to " + COMPLETED
  return HttpResponse(output, content_type="text/plain")

# parameters: Chore ID, giver, reciever
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: chore becomes assigned to reciever on success
# use case: user trades chore to someone else
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
  if chore.assigned_to != GIVER_PERSON_ID:
    output = "Person " + giver.name + " is not assigned to chore " + chore_info.name
    return HttpResponse(output, content_type="text/plain")

  chore.assigned_to = RECIEVER_PERSON_ID
  reciever = Person.objects.get(pid=RECIEVER_PERSON_ID)
  chore.save()

  notification = Notification(chore_info=chore.chore_info_id, action=Notification.ACTIONS.CHANGED.value)
  notification.save()

  output = "Chore " + chore_info.name + " is now assigned to " + reciever.name + " from " + giver.name
  return HttpResponse(output, content_type="text/plain")

# parameters: Household ID
# preconditions: household created and choreinfos/people been defined, chores have been assigned 
# postconditions: no database changes made
# use case: to display the chore schedule for a household
def view_chore_schedule(request):
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

