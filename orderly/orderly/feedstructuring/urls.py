from django.urls import path 
from . import views 

appname = 'feedstructuring'
urlpatterns = [
  path('', views.index, name='index'),
  path('feed/rss', views.LatestEntriesFeed(), name='feed')
]