from django.contrib import admin
from store.models import StoreItem


@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "default_order"]
