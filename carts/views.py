from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
# Create your views here.
from Physical.models import Products ,Detail
def view(request):
    #price=1
    #print(Cart.objects.all())
    try:
        the_id = request.session['cart_id']
    except:
        the_id= None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}
    else:
        empty_message = "Your Cart is empty, Please add Items"
        context = {"empty":True, 'empty_message':empty_message}
   
    template = "cart/view.html"
    return render(request, template, context)

def update_cart(request, slug):
    #price=1
    request.session.set_expiry(12000)
    try:       
        price = request.GET.get('price')
    except:
        qty = None
        update_qty = False
    try:
       the_id =  request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
        #create cart id 

    cart = Cart.objects.get(id=the_id)
    try:
        print('Exe start')
        product = Products.objects.get(id=slug)
        imei = Detail.objects.get(product=product)
        print("The item imei is "+str(imei))
        print('Executed the try statement')
    except Products.DoesNotExist:
        pass
    except:
        pass
    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product,)
    if created:
        print('YAY!!')
    if price:
        cart_item.imei = imei
        cart_item.price = price
        cart_item.save()
    else:
        cart_item.delete()
    #cart_item.save()
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    request.session['items_total'] = cart.cartitem_set.count()
    return HttpResponseRedirect(reverse("cart:cart"))
