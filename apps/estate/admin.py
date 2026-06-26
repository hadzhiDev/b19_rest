from django.contrib import admin

from .models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("number", "area", "floor", "rooms_count", "deadline", "type")
    list_filter = ("type", "floor")
    search_fields = ("number",)
