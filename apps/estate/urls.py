from django.urls import path

from . import views



urlpatterns = [
    path("apartments/", views.apartments_list,)
]