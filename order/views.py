from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from cart.models import CartItem
from cart.cart import Cart
# from front.models import Item
from .models import Order, OrderItem


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
        total_of_items = cart.get_item_total()
        # for i in item_qty.values():
        #     total_of_items += float(i['subtotal'])
        print(total_of_items)
        return render(request, 'order/checkout.html', {
            'cart_items': cart_items,
            'item_qty': item_qty,
            'subtotal': total_of_items,
        })


def place_order(request):
    cart = Cart(request)
    subtotal = cart.get_item_total()
    if request.method == 'POST':
        value = request.POST['shipping']
        payment = request.POST['payment']
        total = subtotal + float(value)
        user = request.user
        full_name = f'{user.profile.first_name} {user.profile.last_name}'
        new_order = Order(user=request.user,
                          full_name=full_name, t_amount=total)
        new_order.save()
        items = cart.get_item()
        item_qty = cart.get_quantity()
        for k, v in item_qty.items():
            for item in items:
                if k == str(item.id):
                    quantity = int(v['quantity'])
                    # print(quantity, type(quantity))
                    order_item = OrderItem(
                        order=new_order, user=user, item=item, qty=quantity, subtotal=(item.price * quantity))
                    order_item.save()
        cart.remove_all(user_id=request.user.id)

        # email = request.POST['email']
        # print(value, payment, total)
        return HttpResponse(f'Order Placed Successfully. Your Order Id - {new_order.pk}')


def testpage(request):

    return render(request, 'order/test.html', {

    })


def order_detail(request):
    pass


def all_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        item_context = {

        }
        for order in orders:
            order_items = OrderItem.objects.filter(order=order)
            item_context[order.id] = order_items

        for key, value in item_context.items():
            for v in value:
                print(v.item.name)
        return render(request, 'order/orders.html', {
            "all_orders": orders,
            'item_context': item_context,
        })
