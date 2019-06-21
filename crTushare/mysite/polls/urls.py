from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('learn', views.learn, name='learn'),
    path('realtime/<str:code>', views.realtime, name='realtime'),
    path('basic', views.basic, name='basic'),
    path('banshare', views.banshare, name='banshare'),
    path('history', views.history, name='history'),
    path('daily', views.daily, name='daily'),
    path('volslowdown', views.volumndowngreen, name='volumndowngreen'),
    path('volumerisered', views.volumerisered, name='volumerisered'),
    path('volhalf', views.volumnhalf, name='volumnhalf')
]