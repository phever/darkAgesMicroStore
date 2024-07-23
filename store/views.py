from django.conf import settings
from django.shortcuts import render
from store.models import StoreItem


def index(request):
    context = {
        'title': settings.STORE_TITLE,
        'title_font': settings.TITLE_FONT.replace(' ', '+'),
        'title_font_class': settings.TITLE_FONT.lower().replace(' ', '-'),
        'items': StoreItem.objects.filter(visible=True).order_by('default_order'),
        'made_by': settings.MADE_BY,
        'name': settings.YOUR_NAME,
        'discord_handle': settings.DISCORD_HANDLE,
    }
    return render(request, 'index.html', context)
