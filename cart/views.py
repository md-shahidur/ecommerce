from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem


# Create your views here.


@login_required
def cart_detail(request, user_id):
    print(user_id)
    cart_items = CartItem.objects.filter(user_id=user_id)
    # cart_items = get_list_or_404(CartItem, user_id=user_id)
    print(cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
    })


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass
