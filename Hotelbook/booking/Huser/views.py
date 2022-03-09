import sys
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Hadmin.models import User, Area, Detail, Gallary, Booking, Wishlist, contact1, Feedback
from Hadmin.form import UserForm, detailForm
from datetime import date
from django.core.mail import send_mail
from django.conf import settings



def show(request):
    hd = Detail.objects.all()
    g = Gallary.objects.all()
    y = request.session['email']
    abc = User.objects.filter(email=y)
    return render(request, 'home.html', {'hd': hd, 'g': g, 'abc':abc})



def register(request):
    a = Area.objects.all()
    r = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        print('---', form)
        if form.is_valid():
            try:
                form.save()
                print('--------', form)
                messages.success(request, 'successfully  data passed')
                return redirect('/login/')
            except:
                pass
        else:
            pass
    else:

        form = UserForm()
    return render(request, 'register.html', {'form': form, 'r': r, 'a': a})


def login(request):
    if request.method == 'POST':
        e = request.POST["email"]
        p = request.POST["pwd"]
        val = User.objects.filter(email=e, pwd=p).count()
        if val==1:
            val = User.objects.filter(email=e, pwd=p)
            for items in val:
                request.session['id']=items.id
                request.session['email']=items.email
                request.session['pwd']=items.pwd
                return redirect('/view/')
        else:
            messages.error(request, 'invalid data')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


def logout(request):
    del request.session['email']
    return redirect('/login/')


def hotel_detail(request):
    hd = Detail.objects.all()
    return render(request, 'hotel.html', {'hd':hd})


def show_detail(request, id):
    hd = Detail.objects.get(id=id)
    d = Detail.objects.all()
    return render(request, 'hotel-show.html', {'hd':hd, 'd':d})


def about(request):
    return  render(request, 'about.html')


def all_gallary(request):
    g = Gallary.objects.all()
    return render(request, 'allgallary.html', {'g':g})


def con(request):
    a = request.session['email']
    c = User.objects.filter(email=a)
    if request.method == 'POST':
        try:
            a = request.session['id']
            sub = request.POST['subject']
            msg = request.POST['message']
            form = contact1(email2_id=a, subject=sub, message=msg)
            form.save()
            print('----', form)
            return redirect('/contact/')
        except:
            print('------', sys.exc_info())
    return render(request, 'contact.html', {'c': c})


def booking(request):

    if request.method == 'POST':
        try:
            da = date.today().strftime("%Y-%m-%d")
            uid = request.session['id']
            did = request.POST.get('detail2_id')
            form = Booking(date=da, user_id_id=uid, detail2_id_id=did)
            print('-------', form)
            form.save()
            print('----------', form)
            return redirect('/booking_show/')
        except:
            print('-----', sys.exc_info())
    return redirect('/booking_show/')

def booking_show(request):
    e = request.session['id']
    p = Booking.objects.filter(user_id=e)
    return render(request, 'booking_show.html', {'p': p})


def wishlist_add(request):
    hd = Detail.objects.all()
    if request.method == 'POST':
        try:
            d = date.today().strftime("%Y-%m-%d")
            uid = request.session['id']
            did = request.POST.get('detail_id')
            form = Wishlist(date=d, user_id_id=uid, detail_id_id=did)
            form.save()
            return redirect('/wishlist_show/')
        except:
           print('____', sys.exc_info())
    return render(request, 'hotel-show.html', {'hd':hd})


def wishlist_show(request):
    e = request.session['id']
    ph = Wishlist.objects.filter(user_id=e)
    return render(request, 'wishlist.html', {'ph': ph})


def delete(request,id):
    s = Wishlist.objects.get(id=id)
    s.delete()
    return redirect('/wishlist_show/')


def send(request):
    subject = "Greetings"
    to = "vidhi31vasoya@gmail.com"
    message = "hello how are you"

    if subject and message and to:
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['vidhi31vasoya@gmail.com'])
        except:
            return HttpResponse('Invalid header found.')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

def feedback(request):
    a = request.session['email']

    c = User.objects.filter(email=a)

    if request.method == 'POST':
        try:
            d = date.today().strftime("%Y-%m-%d")
            uid = request.session['id']
            did = request.POST.get('detail_id')
            form = Feedback(date=d, user_id_id=uid, detail_id_id=did)
            form.save()
            return redirect('/show_detail/')
        except:
            print('____', sys.exc_info())
    return render(request, 'hotel-show.html', {'c':c})


