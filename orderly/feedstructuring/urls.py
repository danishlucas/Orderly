from django.urls import path 
from . import views 

appname = 'feedstructuring'
urlpatterns = [
  path('', views.index, name='index'),
  path('feed', views.LatestEntriesFeed(), name='feed'),
  path('feed/<int:notification>', views.get_notification, name='notification')
]