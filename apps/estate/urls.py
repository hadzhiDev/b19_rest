from django.urls import path

from . import views
from . import cb_view



urlpatterns = [
    # # <----> APARTMENT CRUD FBV <---->
    # path("apartments/", views.apartments_list,),
    # path("apartments/create/", views.apartment_create,),
    # path("apartments/<int:pk>/", views.apartment_detail,),
    # path("apartments/put/<int:pk>/", views.apartment_put,),
    # path("apartments/delete/<int:pk>/", views.apartment_delete,),

    # <----> APARTMENT CRUD CBV <---->
    path("apartments/", cb_view.ApartmentListCreateView.as_view(),),
    path("apartments/<int:pk>/", cb_view.ApartmentRetrieveUpdateDestroyView.as_view(),),
    # path("apartments/<int:pk>/", views.apartment_detail,),
    # path("apartments/put/<int:pk>/", views.apartment_put,),
    # path("apartments/delete/<int:pk>/", views.apartment_delete,),
    
]