from front.models import Item
from .models import CartItem
from django.contrib.auth.models import User


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get existing session key

        cart = self.session.get('session_key')

        # For new user, create new session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            # Add previous Cart items from Cart DB.

        # Make cart available in all pages

        self.cart = cart

    def add(self, item):
        item_id = str(item.id)

        # Logic to check if Item is already in Cart
        if item_id in self.cart:
            msg = 'yes'
            return msg
        else:
            self.cart[item_id] = {'name': item.name, 'price': str(item.price)}

        self.session.modified = True

    def remove(self, item_id):
        # self.item_id = str(item_id)
        item_name = self.cart[item_id]['name']
        print(item_name)
        del self.cart[item_id]
        self.session.modified = True
        return f'Item {item_name} removed from Cart successfully'

    def __len__(self):
        return len(self.cart)

    def get_item(self):
        # Get ids from cart
        item_ids = self.cart.keys()
        #  Use ids to get items from DB
        items = Item.objects.filter(id__in=item_ids)

        return items
