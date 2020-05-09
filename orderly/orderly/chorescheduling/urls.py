from django.urls import path 
from . import views 

appname = 'chorescheduling'
urlpatterns = [
  path('create-schedule', views.create_schedule, name='create_schedule')

  # path('', views.test1, name='test1'),
  # path('template', views.test2, name='test2'),
  # path('<int:household>/', views.test3, name='test3')
]