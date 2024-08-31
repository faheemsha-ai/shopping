from django.shortcuts import render , redirect
from . forms import  LoginForm , ProductForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 
from . models import Product, CartItem

def index(request):
    pro=Product.objects.all()
    fr=Product.objects.filter(cate="Fruit")
    gr=Product.objects.filter(cate="Groccery")
    el = Product.objects.filter(cate="Electronics")
    vg = Product.objects.filter(cate="Vegitbales")
    context={
        pro:"pro",
        "fr":fr,
        "gr":gr,
        "el":el,
        "vg":vg
    }
    return render(request,'index.html',context)

def login(requets):
    form = LoginForm()
    if requets.method == 'POST':
        form = LoginForm(requets.POST)
        if form.is_valid():
            form.save()
            form = LoginForm()
            return redirect("/")
    return render(requets,'login.html',{"form":form})

def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,'reg.html',{"form":form})


@login_required
def product(requets):
    form = ProductForm()
    if requets.method == 'POST':
        form = ProductForm(requets.POST, requets.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return redirect("/")
    return render(requets,'product.html',{"form":form})

@login_required 
def view_cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    print(cart_items)
    total_price=sum(int(item.product.price) * item.quantity for item in cart_items)
    return render(request,"cart.html",{"cart_items":cart_items,"total_price":total_price})
