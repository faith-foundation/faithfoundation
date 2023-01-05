from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('events/', views.event_form, name="events"),
    path('photos/', views.photos, name="photos"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
