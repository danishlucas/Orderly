from django.db import models
from chorescheduling.models import Chore
from enum import Enum

# Create your models here.

# Notification object for actions taken
class Notification(models.Model):
    # Types of actions
    class ACTIONS(Enum):
        COMPLETED = 0
        CHANGED = 1

    ACTION_SEQUENCE = (
        (ACTIONS.COMPLETED, "Completed"),
        (ACTIONS.CHANGED, "Changed")
    )

    # ID
    id = models.AutoField(primary_key=True)
    # Placeholder reference to the updated action
    chore_id = models.ForeignKey('chorescheduling.Chore', on_delete=models.CASCADE)
    # Type of action
    action = models.IntegerField(choices=ACTION_SEQUENCE, default=ACTIONS.COMPLETED)
    # Timestamp of action
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.ACTIONS(self.action).name