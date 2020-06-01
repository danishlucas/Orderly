from django.contrib import admin
from .models import Household, Schedule, Week, Chore, ChoreInfo, Person

# Register your models here.
admin.site.register(Household)
admin.site.register(Schedule)
admin.site.register(Week)
admin.site.register(Chore)
admin.site.register(ChoreInfo)
admin.site.register(Person)