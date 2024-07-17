from django.conf import settings
from django.shortcuts import render
from store.models import StoreItem


def index(request):
    context = {
        'title': settings.STORE_TITLE,
        'items': StoreItem.objects.filter(visible=True),
    }
    return render(request, 'index.html', context)
