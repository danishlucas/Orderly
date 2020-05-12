from django.urls import path 
from . import views 

appname = 'choremanagement'
urlpatterns = [
  path('', views.index, name='index'),
]