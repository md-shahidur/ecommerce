from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Item, Category
from cart.models import CartItem

# Create your views here.


def index(request):
    all_items = Item.objects.all()
    # user = request.user
    # if user:
    #     all_cart_items = CartItem.objects.filter(user=user.id)
    #     cart_item_count = len(all_cart_items)
    #     print(f'Cart Items:{cart_item_count}')
    for item in all_items:
        print(item.price)
        print(item.category, type(item.category))
    return render(request, 'front/index.html', {
        'items': all_items
    })


def item_detail(request, item_id):
    print(item_id)
    item = Item.objects.get(id=item_id)
    print(item)
    return render(request, 'front/shop-detail.html', {
        'item': item
    })
