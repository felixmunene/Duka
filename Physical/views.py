from django.shortcuts import render, redirect 
from django.urls import reverse
from Physical.models import Products,Detail,Sales
from django.views.generic import CreateView, UpdateView
from Physical.forms import ProductsForm,UpdateProducts
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
#from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm, saleform
from django.contrib import messages
# Create your views here.
def dashboard(request,*args,**kwargs):
    query_set = Products.objects.values('id','name','product_model','product_type','quantity')
    #results_list = [entry for entry in query_set]

    return render(request,"Physical/index.html",{"results_list":query_set})

class ProductCreateView(CreateView):
    model = Products
    form_class = ProductsForm
    def get_success_url(self):
        return reverse('dashboard')


def updatestock(request,*args,**kwargs):
    if request.method == 'POST':
        myform = UpdateProducts(request.POST)
        if myform.is_valid():
            #print('This is my form '+str(myform))
            prod_name = myform.cleaned_data.get('name')
            #print('This is my product '+str(prod_name))
            qty = myform.cleaned_data['quantity']
           
            for value in Products.objects.filter(name=prod_name).values_list('quantity'):
                print (value)
                print(value[0])
                if qty > -1:
                    #print(str(value[0])+' is greater than -1')
                    Products.objects.filter(name=prod_name).update(quantity=value[0]+qty)
                else:
                    print('negative values not allowed')
            #print(originalqty)
            #originalqty = prod.quantity
            #updatedqty = originalqty + qty
            #print('This is my updated quantity'+updatedqty)
            #print('This is my quantity '+str(qty))
            
            return redirect(reverse('Physical:dashboard'))

    else:    
        myform = UpdateProducts
    return render(request, 'Physical/products_update_form.html',{'form':myform})

def sellstock(request,*args,**kwargs):
    #context ={}
    query_set = Detail.objects.all()
    
    #imei_set = Detail.objects.all()
    #context = {}
    #results_list = [entry for entry in query_set]

    return render(request,"Physical/products_sale.html",{"results_list":query_set})
#@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    print('This item to be added to cart'+str(product_id))
    try:
        product = get_object_or_404(Products, id=product_id)
        print(product)
        cart.add(product=product, quantity=1)
        messages.info(request, 'Item added to cart')
        print(cart.values())
    except:
        print("Cart Error")
        messages.error(request, 'Cart Error')    
    #print('This is your cart: '+cart)
    # cart = Cart(request)
    # product = get_object_or_404(Products, id=product_id)
    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(product=product,
    #              quantity=cd['quantity'],
    #              update_quantity=cd['update'])
    #     #print('This is your cart :'+cart)
    return redirect('Physical:dashboard')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'Physical/cart_detail.html', {'cart': cart})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                         slug=slug, 
                                         available=True)

    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form})               

def sale_done(request, *args, **kwargs):
    print('activated function')
    if request.method == 'POST':
        print('method is post')
        myform = saleform(request.POST)
        print(myform)
        if myform.is_valid():
            print('processing form')
            print(myform)
            #print('This is my form '+str(myform))
            item_name = myform.cleaned_data.get('Item')
            print(item_name)
            quantity = 1
            #print('This is my product '+str(prod_name))
            imei = myform.cleaned_data['Imei']
            price = myform.cleaned_data['Price']
           
            for value in Products.objects.filter(name=item_name).values_list('quantity'):
                print (value)
                print(value[0])
                if qty > -1:
                    #print(str(value[0])+' is greater than -1')
                    Products.objects.filter(name=prod_name).update(quantity=value[0]-qty)
                    obj = Sales.objects.create(Imei=Imei,product_model=item_name,selling_price=price)
                    obj.save()
                    Detail.objects.filter(Imei=Imei).update(sold=True)

                else:
                    print('negative values not allowed')
            #print(originalqty)
            #originalqty = prod.quantity
            #updatedqty = originalqty + qty
            #print('This is my updated quantity'+updatedqty)
            #print('This is my quantity '+str(qty))
            
            return redirect(reverse('dashboard'))

    else:
        print('reassigning form')   
        myform = saleform()
    return render(request, 'cart/view.html',{'form':myform})
    #return render(request),'Physical/index.html'