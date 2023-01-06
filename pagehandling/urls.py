from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('event-view/', views.event_view, name="event-view"),
    path('photos/', views.photos, name="photos"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
