from django.shortcuts import render, redirect
from .models import User, Area, Detail, Booking,Wishlist
from .form import UserForm, areaForm, detailForm, gallaryForm, bookingForm,wishlistForm
from .function import handle_uploaded_file

def index(request):
    a = User.objects.all()
    y = request.session['email']
    ab = User.objects.filter(email=y)
    return render (request, 'index.html' , {'a':a, 'ab':ab})


def create_user(request):
    a = Area.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        print('---', form)
        if form.is_valid():
            try:
                form.save()
                print('---------',form)
                return redirect('/Hadmin/create_user/')
            except:
                pass
        else:
            pass
    else:
        form = UserForm()
    return render(request, 'user.html',{'form':form, 'a':a})

def table(request):
    s = User.objects.all()
    return render(request, 'tables.html', {'s': s})

def areas(request):
    a = Area.objects.all()
    if request.method == "POST":
        form = areaForm(request.POST)
        print('---', form)
        if form.is_valid():
            try:
                form.save()
                print('---------',form)
                return redirect('/Hadmin/areas/')
            except:
                pass
        else:
            pass
    else:
        form = UserForm()
    return render(request,'area.html',{'form':form, 'a':a})


def details(request):
    d = Area.objects.all()
    if request.method == 'POST':
        form = detailForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img'])
                form.save()
                return redirect('/Hadmin/details/')
            except:
                pass
        else:
            pass
    else:
        form=detailForm()
    return render(request, 'user_detail.html', {'form':form, 'd':d})


def gallary(request):
    g = Detail.objects.all()
    if request.method == 'POST':
        form = gallaryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img1'])
                form.save()
                return redirect('/Hadmin/gallary/')
            except:
                pass
        else:
            pass
    else:
        form = gallaryForm()
    return render(request, 'gallary.html', {'form':form , 'g':g})


def booking(request):
    b = Booking.objects.all()

    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Hadmin/index/')
            except:
                pass
        else:
            pass
    else:
        form = bookingForm()
    return  render(request, 'booking.html', {'form':form , 'b':b})


def wishlists(request):
    w = Wishlist.objects.all()

    if request.method == 'POST':
        form = wishlistForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Hadmin/booking/')
            except:
                pass
        else:
            pass
    else:
        form = wishlistForm()
    return  render(request, 'wishlists.html', {'form':form , 'w':w})