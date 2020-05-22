from django.urls import path 
from . import views 

appname = 'chorescheduling'
urlpatterns = [
  path('create-user', views.create_user, name='create_user'),
  path('login-user', views.login_user, name='login_user'),
  path('logout-user', views.logout_user, name='logout_user'),
  path('get-user-details', views.get_user_details, name='get_user_details'),
  path('get-schedule-details', views.get_schedule_details, name='get_schedule_details'),
  path('create-household', views.create_household, name='create_household'),
  path('add-users', views.add_household_users, name='add_household_users'),
  path('add-chores', views.add_household_chores, name='add_household_chores'),
  path('generate-schedule', views.generate_schedule, name='generate_schedule')

  # path('', views.test1, name='test1'),
  # path('template', views.test2, name='test2'),
  # path('<int:household>/', views.test3, name='test3')
]