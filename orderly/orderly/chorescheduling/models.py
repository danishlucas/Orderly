from django.db import models

class Household(models.Model):
  household_id = models.AutoField(primary_key=True)
  # household_name
  # admin
  
  def __str__(self):
    return "Household " + str(self.household_id)

class Schedule(models.Model):
  schedule_id = models.AutoField(primary_key=True)
  num_weeks = models.IntegerField()
  linked_household = models.OneToOneField('Household', on_delete=models.CASCADE)

  def __str__(self):
    return "Schedule " + str(self.schedule_id) + " - hh " + str(self.linked_household.household_id)

class Week(models.Model):
  week_id = models.AutoField(primary_key=True)
  week_num = models.IntegerField() # ranges from [0, number of weeks in schedule]
  linked_schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE) # many-to-one relationship with schedule

  def __str__(self):
    return "Week " + str(self.week_num) + " - sched " + str(self.linked_schedule.schedule_id)
  
class Chore(models.Model):
  chore_id = models.AutoField(primary_key=True)
  chore_info = models.ForeignKey('ChoreInfo', on_delete=models.CASCADE) # many-to-one relationship with choreinfo
  linked_week = models.ForeignKey('Week', on_delete=models.CASCADE) # many-to-one relationship with week
  assigned_to = models.ForeignKey('Person', on_delete=models.PROTECT) # many-to-one relationship with person
  # status 
  # deadline
  # household id

  def __str__(self):
    return "Chore " + str(self.chore_id) + " - wk " + str(self.linked_week.week_num)

class ChoreInfo(models.Model): 
  chore_info_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=100)

  def __str__(self):
    return "ChoreInfo " + self.name

class Person(models.Model): # see if we can add these fields to user instead
  person_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  # email id
  # password
  # household id
  # status

  def __str__(self):
    return "Person " + self.name