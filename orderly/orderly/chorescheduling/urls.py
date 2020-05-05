from django.urls import path 
from . import views 

appname = 'chorescheduling'
urlpatterns = [
  path('', views.index, name='index'),
  path('template', views.customtemplate, name='customtemplate'),
  path('<int:household>/', views.gethousehold, name='gethousehold')
]