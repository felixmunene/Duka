from decimal import Decimal
from django.conf import settings
from Physical.models import Products


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

       #add item to cart 
    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        products = Products.objects.filter(name=product).values_list('id')
        names =  products = Products.objects.filter(name=product).values_list('name')
        product_id = str(products[0])
        print(product)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'name': str(names[0])}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    def __iter__(self):
        """
            Iterate over the items in the cart and get the products 
            from the database.
            """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Products.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        #for item in self.cart.values():
            #item['price'] = Decimal(item['price'])
            #item['total_price'] = item['price'] * item['quantity']
            #yield item