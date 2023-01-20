from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from userhandling.views import login_user, logout_user, register_user
from photohandling.views import photo_album_view, photo_joseph
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('event-view/', views.event_view, name="event-view"),
    path('event-registration/', views.event_form, name="event-registration"),
    path('event-registration/', views.event_Reg, name="event-reg"),
    path('photos/', views.photos, name="photos"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('register_user', register_user, name="register"),
    path('photo-view', photo_album_view, name="photo-view"),
    path('joseph', photo_joseph, name="joseph"),
    # Passwords management starts here
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)