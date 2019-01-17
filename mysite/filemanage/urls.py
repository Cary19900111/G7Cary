from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('downfile/<str:filename>', views.downfile, name='downfile')
]