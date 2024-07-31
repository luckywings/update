from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import Cart, Product
from django.contrib import messages
from .models import Order, OrderItem
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def product_list(request):
    product=Product.objects.all() 
    return render(request, "product_list.html",{"product":product})

def single_product(request):
    return render(request, "single_product.html")
def blog(request):
    return render(request, "blog.html")
def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
def single_blog(request):
    return render(request, "single_blog.html")
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists!!!!")
        
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken!!!!")
      
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('/')
    else:
       return render(request, "login.html")
    
def contact(request):
    return render(request, "contact.html")

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
  
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        product=request.POST['product']
        quantity=request.POST['quantity']
        address=request.POST['address']
        zipcode=request.POST['zipcode']
        place=request.POST['city']
        phone=request.POST['phone']
        paid_amount=request.POST['total']
        print(first_name)
        order=Order.objects.create(first_name=first_name,last_name=last_name,product=product,quantity=quantity,address=address,zipcode=zipcode,place=place,phone=phone,paid_amount=paid_amount)


    context = {
       "total_price":total_price,
       "cart_items":cart_items
      
    }
    return render(request, "checkout.html",context)

def cart(request):
    cart = Cart.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html',{"cart":cart,"total_price":total_price})
def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')
def confirmation(request):
    return render(request, "confirmation.html")

def elements(request):
    return render(request, "elements.html")

def start_order(request):
    cart = Cart(request)

    if request.method == 'POST':
        username = request.POST.get('username')
       
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        product=request.POST.get('product')

        order = Order.objects.create(user=request.user, username=username, email=email, phone=phone, address=address, zipcode=zipcode, place=place,product=product)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.total_price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        return redirect('product_list')
    return redirect('cart')