from django.db import models

# Create your models here.
class ChoreSchedule(models.Model):
  is_finished = models.BooleanField(default=False)