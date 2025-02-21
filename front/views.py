from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Item, Category
from cart.models import CartItem
from cart.cart import Cart

# Create your views here.


def index(request):
    all_items = Item.objects.all()
    # user = request.user
    # if user:
    #     all_cart_items = CartItem.objects.filter(user=user.id)
    #     cart_item_count = len(all_cart_items)
    #     print(f'Cart Items:{cart_item_count}')
    if request.user.is_authenticated:
        item_id = [item.id for item in all_items]
        # print(item_id)
        cart = Cart(request)
        cart.db_to_cart(item_id=item_id, user=request.user)
    # for item in all_items:
    #     print(item.price)
    #     print(item.category, type(item.category))
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
