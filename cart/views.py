from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from flask import redirect
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
            # quantity = request.POST['quantity']
            item_id = int(request.POST['item_id'])
            item = Item.objects.get(id=item_id)
            cart_items = CartItem.objects.all()
            for i in cart_items:
                if i.item.name == item.name:
                    print('yes already added')
                    msg = {'result': 'Already Added', 'status': 'fail'}
                    return JsonResponse(msg)
                else:
                    print('Not added yet')
                    item_name = item.name
                    msg = {'result': item_name, 'status': 'success'}
                    return JsonResponse(msg)
            # print(cart_items)
            # if item in cart_items:
            #     print('Yes')
            # else:
            #     print('No')

            # print(type(user), type(item))
            # cart_entry = CartItem(item=item, user=user)
            # cart_entry.save()
            # return HttpResponse('Item Added to Cart.')
        else:
            print('Not Working')
    # msg = {'result': item_name}
    # return JsonResponse(msg)


def cart_delete(request):
    if request.method == 'POST':
        user_id = int(request.POST['user_id'])
        cart_item_id = request.POST['cart_item_id']
        cart_item = CartItem.objects.filter(id=cart_item_id)[0]
        cart_item_name = cart_item.item.name
        print(user_id, type(user_id))
        cart_item.delete()
        # return redirect('cart:cart_detail', user_id=user_id)
        # return redirect('front:home')

    msg = {'result': cart_item_name}
    return JsonResponse(msg)


def cart_update(request):
    pass
