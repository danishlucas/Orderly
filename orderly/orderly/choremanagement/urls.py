from django.urls import path 
from . import views 

appname = 'choremanagement'
urlpatterns = [
  path('', views.index, name='index'),
  path('change-chore-completion-status', views.change_chore_completion_status, name='change_chore_completion_status'),
  path('change-chore-assignment', views.change_chore_assignment, name='change_chore_assignment'),
  path('view-chore-schedule', views.view_chore_schedule, name='view_chore_schedule'),
]