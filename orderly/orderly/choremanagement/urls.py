from django.urls import path 
from . import views 

appname = 'choremanagement'
urlpatterns = [
  path('', views.index, name='index'),
  path('change-chore-completion-status', views.change_chore_completion_status, name='change_chore_completion_status'),
  path('change-chore-assignment', views.change_chore_assignment, name='change_chore_assignment'),
  path('view-household-chore-schedule', views.view_household_chore_schedule, name='view_household_chore_schedule'),
  path('view-individual-chore-schedule', views.view_individual_chore_schedule, name='view_individual_chore_schedule'),
  path('get-chore-info', views.get_chore_info, name='get_chore_info')
]