from django.shortcuts import render,redirect
from user.models import Blog,Student,Product,Order,Wishlist
from user.form import BlogForm,ProductForm,StudentForm ,OrderForm,WishlistForm
import sys
# Create your views here.
def register(request):
    if request.method=='POST':
        b=StudentForm(request.POST)
        if b.is_valid():
            b.save()
            return redirect('/2/login/')
        else:
            pass
    else:
        form=StudentForm()
    return render(request,'register.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        a=Student.objects.filter(username=username,password=password).count()
        print("++++",a)
        if a==1:
            a=Student.objects.filter(username=username,password=password)
            for val in a:
                request.session['id']=val.id
                request.session['username']=val.username
                request.session['password']=val.password
                return redirect('/2/home/')
        else:
            pass
    else:
        return render(request,'login.html')
def logout(request):
    del request.session['username']
    return redirect('/2/login/')
        

def home(request):
    b=Blog.objects.all()
    a=Product.objects.all()
    return render(request,'home.html',{'b':b,'a':a})

def product_details(request,id):
    b=Product.objects.get(id=id)
    return render(request,'product_details.html',{'b':b})

def addcart(request):
    if request.method=='POST':
        try:
            a=request.session['id']
            b=request.POST.get('pid')
            c=request.POST['quantity']
            reg=Order(sid_id=a,pid_id=b,quantity=c)
            print('---------', reg)
            reg.save()
            return redirect('/2/shop/')
        except:
            print('++++',sys.exc_info())
    return redirect('/2/home/')

def cart(request):
    b=Order.objects.all()
    return render(request,'cart.html',{'b':b})


def wishlist(request):
    if request.method=='POST':
        try:
            a=request.session['id']
            b=request.POST.get('pid')
            reg=Wishlist(sid_id=a,pid_id=b)
            print('++++',reg)
            reg.save()
            return redirect('/2/shop/')
        except:
            print('++++',sys.exc_info())
        return redirect('/2/home/')

def wishlist_show(request):
    b=Wishlist.objects.all()
    return render(request,'wishlist.html',{'b':b})
def shop(request):
    b=Product.objects.all()
    p=Blog.objects.all()
    return render(request,'shop.html',{'b':b,'p':p})

def shop_sub(request,id=0):
    p = Product.objects.filter(pid=id)
    return render(request,'shop_sub.html',{'p':p})
    
def details(request,id):
    b=Product.objects.get(id=id)
    return render(request,'details.html',{'b':b})



