from django.shortcuts import render
from django.http import HttpResponse
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person

# househould create 
# blank schedule created w/ 5 weeks, defined 3 choreinfos and 3 people 
# GOAL: ASSIGN CHORES AND WEEKS

# Create your views here.
def index(request):
  return HttpResponse("This is the chore scheduling app")

def gethousehold(request, household):
  response = "Household is %s"
  return HttpResponse(response % household)

def customtemplate(request):
  # chore_schedule = ChoreSchedule(is_finished=True)

  # context = {'passed_boolean' : chore_schedule.is_finished, 
  #            'true_text' : "this is TRUEEEE", 
  #            'false_text' : "this is FALSEEE"}
  # return render(request, 'chorescheduling/customtemplate.html', context)
  return HttpResponse("This is the chore scheduling app 2")