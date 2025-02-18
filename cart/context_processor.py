from .cart import Cart


# Create context processor so cart works in all pages.
def cart(request):
    return {'cart': Cart(request)}
