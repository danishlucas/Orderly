from django.shortcuts import render
from django.http import HttpResponse
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person

# preconditions: household, schedule generated and choreinfos/people been defined 
# postcondition: within schedule, weeks generated and within weeks, list of chores assigned to people
def create_schedule(request):
  HOUSEHOLD_ID = 3 # needs to be passed in as a parameter

  household = Household.objects.get(hid=HOUSEHOLD_ID)
  schedule = Schedule.objects.get(linked_household__hid=household.hid) # ... throws exception if can't find, so surround with try/catch
  
  persons = Person.objects.all()
  chore_infos = ChoreInfo.objects.all()

  week_list = []
  for x in range(0, schedule.num_weeks):
    week = Week(week_num=x, linked_schedule_id=schedule.sid)
    week.save()
    week_list.append(week)

  # creating chores for each week 
  for week in week_list:
    for x in range(0, len(chore_infos)): 
      ciid = chore_infos[x].ciid
      wid = week.wid 
      pid = persons[x].pid # ONLY WORKS IF NUM CHORES = NUM PEOPLE, FIND BETTER WAY
      chore = Chore(chore_info_id=ciid, linked_week_id=wid, assigned_to_id=pid)
      chore.save()

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