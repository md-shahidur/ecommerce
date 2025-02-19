class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get existing session key

        cart = self.session.get('session_key')

        # For new user, create new session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

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
