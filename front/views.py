from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from cart.cart import Cart
from cart.models import CartItem
from .models import Item, Category


# Create your views here.


def index(request):
    all_items = Item.objects.all()
    # user = request.user
    # if user:
    #     all_cart_items = CartItem.objects.filter(user=user.id)
    #     cart_item_count = len(all_cart_items)
    #     print(f'Cart Items:{cart_item_count}')
    if request.user.is_authenticated:
        # item_id = [item.id for item in all_items]
        # print(item_id)
        cart = Cart(request)
        # cart.db_to_cart(item_id=item_id, user=request.user)
        cart.db_to_cart(user=request.user)
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


def shop_page(request):
    categories = Category.objects.all()
    # Get all Items
    all_items = Item.objects.all().order_by('id')
    # Setup paginator
    p = Paginator(all_items, 6)
    page = request.GET.get('page')
    items = p.get_page(page)
    page_range = p.page_range

    return render(request, 'front/shop.html', {
        'categories': categories,
        'all_items': items,
        'page_range': page_range,
    })
