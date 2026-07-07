from django.contrib import admin

from .models import Apartment, Block, Object


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("number", "area", "floor", "rooms_count", "deadline", "type")
    list_filter = ("type", "floor")
    search_fields = ("number",)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("number", "floors_count", "entrance_count", "object__name",)
    list_filter = ("object__name",)
    search_fields = ("object__name",)


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "image")
    list_display_links = ("id", "name")
    search_fields = ("name",)