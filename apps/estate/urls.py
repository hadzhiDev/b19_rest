from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from . import generics_views
from . import viewsets

router = DefaultRouter()
router.register("apartments", viewsets.ApartmentViewSet, basename='apartments')
# router.register("apartments", viewsets.ApartmentViewSet, basename='apartments')
# router.register("apartments", viewsets.ApartmentViewSet, basename='apartments')


urlpatterns = [
    path('', include(router.urls)),
    # # <----> APARTMENT CRUD FBV <---->
    # path("apartments/", views.apartments_list,),
    # path("apartments/create/", views.apartment_create,),
    # path("apartments/<int:pk>/", views.apartment_detail,),
    # path("apartments/put/<int:pk>/", views.apartment_put,),
    # path("apartments/delete/<int:pk>/", views.apartment_delete,),

    # <----> APARTMENT CRUD CBV <---->
    # path("apartments/", generics_views.ApartmentListCreateView.as_view(),),
    # path("apartments/<int:pk>/", generics_views.ApartmentRetrieveUpdateDestroyView.as_view(),),
    # path("apartments/<int:pk>/", views.apartment_detail,),
    # path("apartments/put/<int:pk>/", views.apartment_put,),
    # path("apartments/delete/<int:pk>/", views.apartment_delete,),
    
]