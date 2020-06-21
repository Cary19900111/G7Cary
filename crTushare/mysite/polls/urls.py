from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('learn', views.learn, name='learn'),
    path('realtime/<str:code>', views.realtime, name='realtime'),
    path('basic', views.basic, name='basic'),
    path('banshare/<str:year>/<str:month>', views.banshare, name='banshare'),
    path('history', views.history, name='history'),
    path('daily', views.daily, name='daily'),
    path('getDataByDay/<str:daytime>',views.GetDataByDay,name='getDataByDay'),
    path('volslowdown', views.volumndowngreen, name='volumndowngreen'),
    path('volumerisered', views.volumerisered, name='volumerisered'),
    path('volriseonbottom', views.volRiseOnBottom, name='volRiseOnBottom'),
    path('volhalf', views.volumnhalf, name='volumnhalf'),
    path('volRiseAndDownRecentFourDay',views.volRiseAndDownRecentFourDay,name='volRiseAndDownRecentFourDay'),
    path('github/repo_list',views.get_github_trend,name='get_github_trend'),
    path('toutiao/posts',views.get_toutiao_posts,name='get_toutiao_posts'),
    path('hacker/news',views.get_hacker_news,name='get_hacker_news'),
    path('segmentfault/blogs',views.get_segmentfault_blogs,name='get_segmentfault_blogs'),
    path('GetName',views.GetName,name='GetName')
]