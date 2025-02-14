from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from front.models import Item


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


@login_required
def cart_add(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            user = request.user
            quantity = request.POST['quantity']
            item_id = int(request.POST['item_id'])
            item = Item.objects.get(id=item_id)
            print(type(user), quantity, type(item))
            cart_entry = CartItem(item=item, quantity=int(
                quantity), user=user)
            cart_entry.save()
            # return HttpResponse('Item Added to Cart.')
        else:
            print('Not Working')
    msg = {'result': 'Item Added to Cart'}
    return JsonResponse(msg)


def cart_delete(request):
    pass


def cart_update(request):
    pass
