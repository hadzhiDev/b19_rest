from django.urls import path

from . import views



urlpatterns = [
    # <----> APARTMENT CRUD <---->
    path("apartments/", views.apartments_list,),
    path("apartments/create/", views.apartment_create,),
    path("apartments/<int:pk>/", views.apartment_detail,),
    path("apartments/put/<int:pk>/", views.apartment_put,),
    path("apartments/delete/<int:pk>/", views.apartment_delete,),
    
]