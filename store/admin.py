from django.contrib import admin
from store.models import CustomPage, CustomPageBlock, StoreItem


@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "default_order"]


admin.site.register(CustomPage)
admin.site.register(CustomPageBlock)
