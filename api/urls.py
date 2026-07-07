from django.urls import path, include


urlpatterns = [
    path('', include("apps.estate.urls")),
    path('', include("api.yasg"))
]
