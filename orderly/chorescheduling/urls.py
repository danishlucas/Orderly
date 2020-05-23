from django.urls import path 
from . import views 

appname = 'chorescheduling'
urlpatterns = [
  path('create-user', views.create_user, name='create_user'),
  path('login-user', views.login_user, name='login_user'),
  path('logout-user', views.logout_user, name='logout_user'),
  path('get-active-user', views.get_active_user, name='get_active_user'),
  path('get-user-details', views.get_user_details, name='get_user_details'),
  path('get-full-schedule', views.get_full_schedule, name='get_full_schedule'),
  path('get-week-schedule', views.get_week_schedule, name='get_week_schedule'),
  path('get-household-users', views.get_household_users, name='get_household_users'),
  path('create-household', views.create_household, name='create_household'),
  path('add-users', views.add_household_users, name='add_household_users'),
  path('remove-users', views.remove_household_users, name='remove_household_users'),
  path('add-chores', views.add_household_chores, name='add_household_chores'),
  path('remove-chores', views.remove_household_chores, name='remove_household_chores'),
  path('generate-schedule', views.generate_schedule, name='generate_schedule')

  # path('', views.test1, name='test1'),
  # path('template', views.test2, name='test2'),
  # path('<int:household>/', views.test3, name='test3')
]