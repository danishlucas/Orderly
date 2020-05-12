from django.db import models

# Create your models here.

# Notification object for actions taken
class Notification(models.Model):
    # UUID for primary key
    uuid = models.AutoField(primary_key=True)
    # Placeholder reference to the updated action
    action = models.ForeignKey('Action', on_delete=models.CASCADE)
    # Timestamp of action
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.action

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.uuid)})