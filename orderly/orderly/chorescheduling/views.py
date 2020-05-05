from django.shortcuts import render
from django.http import HttpResponse

from .models import ChoreSchedule

# Create your views here.
def index(request):
  return HttpResponse("This is the chore scheduling app")

def gethousehold(request, household):
  response = "Household is %s"
  return HttpResponse(response % household)

def customtemplate(request):
  chore_schedule = ChoreSchedule(is_finished=True)

  context = {'passed_boolean' : chore_schedule.is_finished, 
             'true_text' : "this is TRUEEEE", 
             'false_text' : "this is FALSEEE"}
  return render(request, 'chorescheduling/customtemplate.html', context)