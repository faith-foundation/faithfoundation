from django.urls import path
from . import views

urlpatterns = [
    path('photo-view', views.photo_album_view, name="photo-view"),
    path('joseph', views.photo_joseph, name="joseph")

]