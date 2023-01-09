from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from userhandling.views import login_user, logout_user, register_user
urlpatterns = [
    path('', views.home, name="home"),
    path('event-view/', views.event_view, name="event-view"),
    path('event-registration/', views.event_form, name="event-registration"),
    path('photo-album/', views.photo_album_view, name="photo-album"),
    path('photos/', views.photos, name="photos"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('register_user', register_user, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)