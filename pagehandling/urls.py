from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('events/', views.event_form, name="events"),
]
