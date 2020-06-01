from django.urls import path 
from . import views 

appname = 'feedstructuring'
urlpatterns = [
  path('', views.index, name='index'),
  path('feed/<int:household_id>', views.LatestEntriesFeed(), name='feed'),
  path('feed/notification/<int:notification>', views.get_notification, name='notification')
]