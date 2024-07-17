from django.shortcuts import render
from store.models import StoreItem


def index(request):
    context = {
        'title': 'Iglis.Shop',
        'items': StoreItem.objects.filter(visible=True),
    }
    return render(request, 'index.html', context)
