from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from cart.models import CartItem
from front.models import Item
from cart.cart import Cart


# Create your views here.


# def order_summery(request):
#     if request.method == "POST":
#         # ids = json.load(request)['ids']
#         # qty = json.load(request)['ids']
#         data = request.POST['data']
#         j_data = json.loads(data)
#         # print(j_data['qty'], type(j_data))
#         id_list = []
#         qty_list = []
#         subtotal = float(j_data['subtotal'])
#         grand_total = float(j_data['total'])

#         for data in j_data['qty']:
#             qty_list.append(int(data))
#         for data in j_data['ids']:
#             id_list.append(int(data))
#         # for data in j_data['total']:
#         #     print(data, type(data))
#         new_dict = {k: v for k, v in zip(id_list, qty_list)}

#         print(new_dict, subtotal, grand_total, type(grand_total))
#         msg = {'result': 'Ajax Success'}
#         return JsonResponse(msg)

def checkout(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_items = cart.get_item
        item_qty = cart.get_quantity()
        total_of_items = 0
        for i in item_qty.values():
            total_of_items += float(i['subtotal'])
        print(total_of_items)
        return render(request, 'order/checkout.html', {
            'cart_items': cart_items,
            'item_qty': item_qty,
            'subtotal': total_of_items,
        })
