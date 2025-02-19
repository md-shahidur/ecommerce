import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CartItem
from front.models import Item
from .cart import Cart


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


# @login_required
# def cart_add(request):
#     if request.user.is_authenticated:

#         if request.method == 'POST':
#             user = request.user
#             # quantity = request.POST['quantity']
#             item_id = int(request.POST['item_id'])
#             item = Item.objects.get(id=item_id)
#             print(item)
#             cart_items = CartItem.objects.all()
#             cart_item_list = [i.item.name for i in cart_items]
#             print(cart_item_list)
#             # for i in cart_items:
#             if item.name in cart_item_list:
#                 print('yes already added')
#                 msg = {'result': 'Already Added', 'status': 'fail'}
#                 return JsonResponse(msg)
#             else:
#                 print('Not added yet')
#                 cart_entry = CartItem(item=item, user=user)
#                 cart_entry.save()
#                 item_name = item.name
#                 msg = {'result': item_name, 'status': 'success'}
#                 return JsonResponse(msg)

#                 # print('Not added yet')

#                 # item_name = item.name
#                 # msg = {'result': item_name, 'status': 'success'}
#                 # return JsonResponse(msg)
#             # print(cart_items)
#             # if item in cart_items:
#             #     print('Yes')
#             # else:
#             #     print('No')

#             # print(type(user), type(item))

#             # return HttpResponse('Item Added to Cart.')
#         else:
#             print('Not Working')
#     # msg = {'result': item_name}
#     # return JsonResponse(msg)


def cart_add(request):
    # Get Cart class object
    cart = Cart(request)

    # Get data back from 'add to cart' button.
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))

        # Get item from DB
        item = get_object_or_404(Item, id=item_id)

        # Add Item to Cart object
        item_to_cart = cart.add(item=item)
        if item_to_cart == 'yes':
            response = JsonResponse(
                {'status': f'{item.name} is already in Cart.'})
        else:
            response = JsonResponse(
                {'status': f'{item.name} is added to the Cart.'})
        return response


@login_required
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
