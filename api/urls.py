from django.urls import path, include


urlpatterns = [
    path('auth/', include("apps.accounts.urls")),
    path('', include("apps.estate.urls")),
    path('', include("api.yasg"))
]
