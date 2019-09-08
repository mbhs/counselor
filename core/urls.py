from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.eventForm, name='index'),
    path('upload/', views.processFile, name='upload'),
    path('events/', views.listEvents, name='events'),
    path('page/<str:st>/', views.contentPage, name='content'),
]
