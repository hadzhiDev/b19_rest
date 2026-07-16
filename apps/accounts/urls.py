from django.urls import path

from . import views



urlpatterns = [
    path("login/", views.custom_login, name="auth_login"),
    path("register/", views.custom_register, name="auth_register"),
    path("profile/", views.profile, name="auth_profile"),
    path("logout/", views.logout, name="auth_logout"),
    path("deactivate/", views.deactivate, name="auth_deactivate"),
]