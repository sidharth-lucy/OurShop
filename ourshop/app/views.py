from itertools import product
from unicodedata import category
from warnings import catch_warnings
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Customer,Product,Cart,OrederPlaced
from django.db.models import Q 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomerRegistrationForm , UserLoginForm ,CustomerProfileForm

@login_required(login_url='/account/login/')
def buy_now(request):

    prod_id = request.POST['prod_id']
    user = request.user
    c= Cart(user= user , product= Product.objects.get(id=prod_id))
    c.save()
    return redirect('/checkout/')



@login_required(login_url='/account/login/')
def checkout(request):
    address = Customer.objects.filter(user= request.user)
    
    item = Cart.objects.filter(user=request.user)
    total_cost =0
    amount= 0
    shipping_charge=0
    if len(item)>0:
        for p in item:
            x= p.quantity 
            y= p.product.discounted_price
            amount+=x*y 
        if amount>0:
            total_cost = amount+70
            shipping_charge = 70.0


    return render(request, 'app/checkout.html' , {
        'address':address ,
        'item':item, 
        'totalcost':total_cost,
    })



@login_required(login_url='/account/login/')
def orders(request):
    orders = OrederPlaced.objects.filter(user= request.user)
    return render(request, 'app/orders.html', {
        'orders':orders,
    })

@login_required(login_url='/account/login/')
def orders_continue(request):

    customer_id = request.GET.get('address_select')
    user = request.user
    customer = Customer.objects.get(id=customer_id)
    # print(customer_id)
    items = Cart.objects.filter(user=user)
    for item in items:
        OrederPlaced(user=user , product= item.product , customer= customer ,quantity= item.quantity).save()
        # item.delete()
    items.delete()
    return redirect('/orders')


@login_required(login_url='/account/login/')
def plus_cart(request):
    if request.method=='GET':
        p_id = request.GET['prod_id']
        # print(p_id)
        # c = Cart.objects.get(Q(product= p_id) & Q(user= request.user))
        c= Cart.objects.get(id=p_id)
        c.quantity+=1 
        c.save()

        products_in_cart = Cart.objects.filter(user=request.user)
        total_cost =0
        amount= 0
        shipping_charge=0
        if len(products_in_cart)>0:
            for p in products_in_cart:
                x= p.quantity 
                y= p.product.discounted_price
                amount+=x*y 
            
            total_cost = amount+70
            shipping_charge = 70.0

        data ={
            'quantity': c.quantity,
            'amount': amount,
            'total_cost': total_cost,
            'shipping_charge': shipping_charge,
        }
        return JsonResponse(data)

@login_required(login_url='/account/login/')
def minus_cart(request):
    if request.method=='GET':
        p_id = request.GET['prod_id']

        c= Cart.objects.get(id=p_id)
        c.quantity-=1 
        c.save()

        products_in_cart = Cart.objects.filter(user=request.user)
        total_cost =0
        amount= 0
        shipping_charge=0
        if len(products_in_cart)>0:
            for p in products_in_cart:
                x= p.quantity 
                y= p.product.discounted_price
                amount+=x*y 
            if amount>0:
                total_cost = amount+70
                shipping_charge = 70.0

        data ={
            'quantity': c.quantity,
            'amount': amount,
            'total_cost': total_cost,
            'shipping_charge': shipping_charge,
        }
        return JsonResponse(data)

@login_required(login_url='/account/login/')
def remove_cart(request):
    if request.method=='GET':
        p_id = request.GET['prod_id']
        Cart.objects.get(id=p_id).delete()

        products_in_cart = Cart.objects.filter(user=request.user)
        total_cost =0
        amount= 0
        shipping_charge=0
        if len(products_in_cart)>0:
            for p in products_in_cart:
                x= p.quantity 
                y= p.product.discounted_price
                amount+=x*y 
            
            total_cost = amount+70
            shipping_charge = 70.0

        data ={
            'amount': amount,
            'total_cost': total_cost,
            'shipping_charge': shipping_charge,
        }
        return JsonResponse(data)



@login_required(login_url='/account/login/')
def add_to_cart(request):
    pro_id = request.POST["prod_id"]
    user = request.user
    Cart(user=user , product= Product.objects.get(id= pro_id)).save()
    return redirect('/show-cart')

@login_required(login_url='/account/login/')
def showcart(request):
    if request.user.is_authenticated:    
        user = request.user
        products_in_cart = Cart.objects.filter(user= user)
        n = len(products_in_cart)

        total_cost =0
        amount= 0
        shipping_charge=0
        if products_in_cart:
            for p in products_in_cart:
                x= p.quantity 
                y= p.product.discounted_price
                amount+=x*y 
            
            total_cost = amount+70
            shipping_charge = 70.0

        return render(request , 'app/addtocart.html' ,{
            "product":products_in_cart,
            'n':n, 
            'amount': amount,
            'total_cost':total_cost,
            'shipping_charge':shipping_charge,
        })


@login_required(login_url='/account/login/')
def deleteAddress(request):
    customerId = request.POST['addId']
    temp= Customer.objects.get(id= customerId)
    temp.delete()
    return redirect('/show-cart')

@login_required(login_url='/account/login/')
def address(request):
    customer_address = Customer.objects.filter(user= request.user)
    return render(request, 'app/address.html' ,{
        'customer_address':customer_address,
        'activeadd':'btn-primary'
    })

# def profile(request):
#  return render(request, 'app/profile.html')

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class UserProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()

        return render(request , 'app/profile.html' ,{
            'form':form,
            'activepro':'btn-primary',
        })

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            # we can use cleaned data to save data also
            temp =form.save(commit=False)
            temp.user= request.user
            temp.save()
            messages.success(request , 'New profile Added Successfully!!')
            return render(request , 'app/profile.html' ,{
            'form':CustomerProfileForm(),
            'activepro':'btn-primary',
            })
        else:
            messages.warning(request , 'Please Try again !!')
            return render(request , 'app/profile.html' ,{
            'form':form,
            'activepro':'btn-primary',
            })


# def change_password(request):
#  return render(request, 'app/changepassword.html')


# def login(request):
#  return render(request, 'app/login.html')


# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request , 'app/customerregistration.html' , {
            'form':form,
        })
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,'Registered Succesfully !!')
        else:
            messages.warning(request , 'Sorry Try again !')
            return render(request , 'app/customerregistration.html' , {
            'form':form,
            })

        return render(request , 'app/login.html')






# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')

        # n= list(range(1,12))
        return render(request , 'app/home.html' ,{
            'topwears':topwears,
            'bottomwears':bottomwears,
            'mobile':mobile,
            'laptop':laptop,
            
        })

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,id):
        product = Product.objects.get(id = id)
        is_carted =False

        if request.user.is_authenticated:
            is_carted = Cart.objects.filter(Q(user=request.user) & Q(product= product)).exists()

        return render(request , 'app/productdetail.html' ,{
            "product":product,
            'is_carted':is_carted,
        })



def mobile(request,data=None):
    allPhone = Product.objects.filter(category= 'M')
    if data==None:
        mobiles = allPhone

    else:
        mobiles = allPhone.filter(brand= data)

    brands = set()
    for item in allPhone:
        b = item.brand
        brands.add(b)

    return render(request, 'app/mobile.html' ,{
        'mobiles':mobiles,
        'brands':brands,
    })



def laptop(request,data=None):
    alllaptop = Product.objects.filter(category= 'L')
    if data==None:
        laptops = alllaptop

    else:
        laptops = alllaptop.filter(brand= data)

    brands = set()
    for item in alllaptop:
        b = item.brand
        brands.add(b)

    return render(request, 'app/laptop.html' ,{
        'laptops':laptops,
        'brands':brands,
    })




def topwear(request,data=None):
    alltopwears = Product.objects.filter(category= 'TW')
    if data==None:
        topwears = alltopwears

    else:
        topwears = alltopwears.filter(brand= data)

    brands = set()
    for item in alltopwears:
        b = item.brand
        brands.add(b)

    return render(request, 'app/topwere.html' ,{
        'topwears':topwears,
        'brands':brands,
    })





def bottomWear(request,data=None):
    allbottom = Product.objects.filter(category= 'BW')
    if data==None:
        bottomwears = allbottom

    else:
        bottomwears = allbottom.filter(brand= data)

    brands = set()
    for item in allbottom:
        b = item.brand
        brands.add(b)

    return render(request, 'app/bottomwere.html' ,{
        'bottomwears':bottomwears,
        'brands':brands,
    })



