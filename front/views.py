from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item, Category

# Create your views here.


def index(request):
    all_items = Item.objects.all()
    for item in all_items:
        print(item.price)
        print(item.category, type(item.category))
    return render(request, 'front/index.html', {
        'items': all_items

    })
