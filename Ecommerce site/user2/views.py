from django.shortcuts import render,redirect
from user.models import Student, Blog,Product,Order,Feedback,Wishlist,gallary,Billing,order_item
from user.form import StudentForm,BlogForm,ProductForm,OrderForm,FeedbackForm,WishlistForm,BillingForm,order_itemForm,gallaryForm
import sys
from django.http import HttpResponse
from datetime import date
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    a = Blog.objects.all()
    b=request.session['username']
    c=Student.objects.filter(username=b)
    return render(request, 'home.html', {'a':a,'c':c})

def register(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        print('++++',form)
        if form.is_valid():
            form.save()
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
    return render(request,'login.html')

def logout(request):
        del request.session['username']
        return redirect('/2/login/')

def email(request):
    subject='hello Django!!!'
    msg='sucess'
    to='raj.kanani9764@gmaii.com'
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  

def product(request):
    b=Product.objects.all()
    return render(request,'home.html',{'b':b})

def addcart(request):
    if request.method == 'POST':
        try:
            a=request.session['id']
            b=request.POST.get('pid')
            c=request.POST['quantity']
            reg=Order(sid_id=a,pid_id=b,quantity=c)
            print('---------', reg)
            reg.save()
            print("++++",reg)
            return redirect('/2/cart/')
        except:
            print('--',sys.exc_info())
    return redirect('/home/')  

def cart(request):
    b=request.session['id']
    c = Order.objects.filter(sid=b)
    return render(request,'cart.html',{"c":c})

def wishlist_show(request):
    b=request.session['id']
    a=Wishlist.objects.filter(sid=b)
    return render(request,'wishlist.html',{'a':a})


def wishlist(request):
    if request.method == 'POST':
        try:
            a=request.session['id']
            b=request.POST.get('pid')
            reg=Wishlist(sid_id=a,pid_id=b)
            print('---------', reg)
            reg.save()
            print("++++",reg)
            return redirect('/2/wishlist_show/')
        except:
            print('--',sys.exc_info())
    return redirect('/2/wishlist_show/')  

def wishlist_show(request):
    b=request.session['id']
    a=Wishlist.objects.filter(sid=b)
    return render(request,'wishlist.html',{'a':a})


def view(request, id):
    b=Product.objects.filter(id=id)
    return render(request,'header2.html',{'p':b})
    
def product_details(request,id):
    b=Product.objects.get(id=id)
    return render(request,'product_details.html',{'b':b})

def shop(request):
    b=Product.objects.all()
    p=Blog.objects.all()
    return render(request,'shop.html',{'b':b,'p':p})

def shop_sub(request,id):
    b=Blog.objects.all()
    p = Product.objects.filter(blog_id=id)
    return render(request,'shop_sub.html',{'p':p,'b':b})

def details(request,id):
    b=Product.objects.get(id=id)
    d=gallary.objects.filter(pid=id)
    return render(request,'details.html',{'b':b,"d":d})

def add(request,id):
    b=Order.objects.get(id=id)
    return render(request,'product_details.html',{'b':b})

def feedback(request):
    b = Product.objects.all()
    if request.method=='POST':
        try:
            a=request.session['id']
            b=request.POST.get('pid')
            c= date.today().strftime('%Y-%m-%d')
            d=request.POST['address']
            e=request.POST['review']
            reg=Feedback(sid_id=a,pid_id=b,date=c,address=d,review=e)
            print('++++',reg)
            reg.save()
            print('++++',reg)
            return redirect('/2/home/')
        except:
            print('+++',sys.exc_info())
    return render(request,'feedback.html', {'b':b})

def checkout(request):
    b=request.session['id']
    a = Order.objects.filter(sid=b)
    if request.method == "POST":
        try:
            b = request.session['id']
            add = request.POST['address']
            app = request.POST['apprtment']
            zip = request.POST['zip']
            country = request.POST['country']
            mal = request.POST['email']
            phone = request.POST['phone']
            form = Billing(user_id=b, address=add, apprtment=app, zip=zip, country= country, email=mal, phone=phone)
            form.save()
            return redirect('/2/home/')
        except:
            print('-------', sys.exc_info())
    return render(request, 'checkout.html',{"a":a})

def final_order(request):
    if request.method=='POST':
        try:
            a=request.session['id']
            bil=Billing.objects.filter(billing=a)
            it=order_item.objects.filter(sid=a)
            ord= date.today().strftime('%Y-%m-%d')
            d=request.POST['ordered']
            form=order_item(user_id=a,billing=bil,item=it,orderdate=ord,ordered=d)
            form.save()
            return redirect('/2/home/')
        except:
            print('+++++++++++',sys.exc_info())
    return render(request,'checkout.html')


def remove_cart(request,id):
    b=request.session['id']
    c=Order.objects.filter(sid=b)
    return redirect('/2/cart/')