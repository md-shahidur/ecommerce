from front.models import Item
from .models import CartItem
from django.contrib.auth.models import User


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        # Get existing session key

        cart = self.session.get('session_key')

        # For new user, create new session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make cart available in all pages

        self.cart = cart

    def add(self, item, quantity):
        item_id = str(item.id)
        subtotal = str(quantity * item.price)
        quantity = str(quantity)

        # Logic to check if Item is already in Cart
        if item_id in self.cart:
            msg = 'yes'
            return msg
        else:
            self.cart[item_id] = {'name': item.name,
                                  'quantity': quantity, 'subtotal': subtotal}
            # self.cart[item_id] = {'name': item.name,
            #                       'price': str(item.price), 'qty': str(qty)}
            cart_db_entry = CartItem(
                item=item, user=self.request.user, quantity=int(quantity), subtotal=float(subtotal))
            cart_db_entry.save()

        self.session.modified = True

    def update_qty(self, item_id, quantity):
        item_id = str(item_id)
        item = Item.objects.get(id=item_id)
        # Login check

        if item_id in self.cart:
            # update quantity in Cart DB
            cart_item = CartItem.objects.get(item_id=item_id)
            cart_item.quantity = quantity
            subtotal = float(int(quantity) * item.price)
            cart_item.subtotal = subtotal
            cart_item.save()
            # update quantity in session
            self.cart[item_id]['quantity'] = quantity
            self.cart[item_id]['subtotal'] = subtotal

            self.session.modified = True

            print(f'yes matched, new quantity is {quantity}')
        else:
            print('Not matched')

    def remove(self, item_id):
        # self.item_id = str(item_id)
        item_name = self.cart[item_id]['name']
        print(item_name)
        del self.cart[item_id]
        self.session.modified = True
        return f'Item {item_name} removed from Cart successfully'

    def remove_all(self, user_id):
        # clear cart from session
        cart = self.cart
        cart.clear()
        # clear cart from db
        cart_db = CartItem.objects.filter(user=user_id)
        cart_db.delete()
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_item(self):
        # Get ids from cart
        item_ids = self.cart.keys()
        #  Use ids to get items from DB
        items = Item.objects.filter(id__in=item_ids)
        return items

    def get_quantity(self):
        quantity = self.cart
        return quantity

    def get_item_total(self):
        cart_items = self.cart
        total_of_items = 0
        for i in cart_items.values():
            total_of_items += float(i['subtotal'])
        return total_of_items

    # def db_to_cart(self, item_id, user):

    def db_to_cart(self, user):
        user_id = user.id
        if self.cart:
            pass
        else:
            cart_db_items = CartItem.objects.filter(user=user_id)
            for item in cart_db_items:
                # print(i.item.id)
                # print(item_id)
                # if i.item.id in item_id:
                #     print('yes item matched')
                #     self.cart[str(i.item.id)] = {
                #         'name': i.item.name, 'price': str(i.item.price)}
                self.cart[str(item.item.id)] = {'name': item.item.name,
                                                'quantity': str(item.quantity), 'subtotal': str(item.subtotal)}
                self.session.modified = True
                # else:
                #     print('Not matched from db')
