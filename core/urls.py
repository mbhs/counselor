from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.eventForm, name='add'),
    path('add/', views.eventForm, name='addForm'),
    path('upload/', views.processFile, name='upload'),
    path('events/', views.listEvents, name='events'),
    path('<str:st>/', views.contentPage, name='content'),
    path('counselors/<str:lastName>/', views.counselorInfo, name="counselor")
]
