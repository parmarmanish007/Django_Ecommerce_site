from django.shortcuts import render,redirect
from.models import Student
from.models import Blog
from.form import RegisterForm,BlogForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from.function.function import handle_uploaded_file
from django.contrib.auth.forms import AuthenticationForm
import sys
# Create your views here.
def home(request):
    return render(request,'index/index.html')
        
def login(request):
    if request.method == "POST":

        e = request.POST.get('username')
        p = request.POST.get('password')
       
        val = Student.objects.filter(username=e, password=p).count()

        if val == 1:
            val = Student.objects.filter(username=e, password=p)
            print("+++++++++++++++++", val)
            for items in val:
        
                request.session['username'] = items.username
                request.session['password'] = items.password
                messages.info(request,'login sucesss')
                return redirect("/home/")
        else:
            messages.error(request, "Invalid username and password")
            return redirect("/register/")
    else:
        return render(request, "security/login.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'user created')
                return redirect('/login/')
            except:
                print('---', sys.exc_info())
        else:
            pass
    else:
        form = RegisterForm()
        return render(request, 'security/register.html', {"form": form})
    return render(request, 'security/register.html', {"form": form})
def edit(request,id):
    b=Student.objects.get(id=id)
    return render(request,'security/edit.html',{'b':b})

def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(id=id)
        form=RegisterForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.info(request,'profile updated')
        else:
            pi=Student.objects.get(id=id)
            form=RegisterForm(instance=pi)
    return render(request,'security/edit.html',{'b':form})

def insert(request):
    b=Blog.objects.all()
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img'])
                form.save()
                return redirect('/blog/')
            except:
                print('+++++++++++++++++', sys.exc_info())
        else:
            pass
    else:
        form = BlogForm()
    return render(request, 'blog/insert.html', {'form': form, 'b': b})


def blog_show(request):
    b=Blog.objects.all()
    return render(request,'index/index.html',{'b':b})


def blog_details(request,id):
    b=Blog.objects.filter(id=id)
    return render(request,'blog/blog_details.html',{'b':b})


def cart(request):
    b=Blog.objects.all()
    return render(request,'order/cart.html',{'b':b})

def contact(request):
    return render(request,'security/contact.html')


def chekout(request):
     return render(request,'order/chekout.html')

def wishlist(request):
    b=Blog.objects.all()
    return render(request,'order/wishlist.html',{'b':b})

def shop(request):
    b=Blog.objects.all()
    return render(request,'order/shop.html',{'b':b})
def single(request):
    b=Blog.objects.all()
    return render(request,'order/single-product.html',{'b':b})

def sidebar(request):
    b=Blog.objects.all()
    return render(request,'order/shop-sidebar.html',{'b':b})

