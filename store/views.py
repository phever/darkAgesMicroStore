from django.conf import settings
from django.shortcuts import get_object_or_404, render
from store.models import CustomPage, StoreItem


def index(request):
    context = {
        "title": settings.STORE_TITLE,
        "title_font": settings.TITLE_FONT.replace(" ", "+"),
        "title_font_class": settings.TITLE_FONT.lower().replace(" ", "-"),
        "items": StoreItem.objects.filter(visible=True).order_by("default_order"),
        "made_by": settings.MADE_BY,
        "name": settings.YOUR_NAME,
        "discord_handle": settings.DISCORD_HANDLE,
        "custom_pages": CustomPage.objects.all().order_by("title"),
    }
    return render(request, "index.html", context)


def custom_page(request, page_name):
    context = {
        "title": settings.STORE_TITLE,
        "title_font": settings.TITLE_FONT.replace(" ", "+"),
        "title_font_class": settings.TITLE_FONT.lower().replace(" ", "-"),
        "made_by": settings.MADE_BY,
        "name": settings.YOUR_NAME,
        "discord_handle": settings.DISCORD_HANDLE,
        "custom_page": get_object_or_404(CustomPage, slug=page_name),
    }
    return render(request, "custom_page.html", context)
