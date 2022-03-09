from django.shortcuts import render,redirect
from.models import Student,Blog,Product,Order,gallary
from.form import StudentForm,BlogForm,ProductForm,OrderForm,gallaryForm
import sys
from.function.function import upload

# Create your views here.
def home(request):
    return render(request,'index.html')

def basic(request):
    if request.method=='POST':
        b=StudentForm(request.POST)
        print('--------', b)
        if b.is_valid():
            try:
                b.save()
                print('----------', b)
                return redirect('/basic/')
            except:
                pass
        else:
            pass
    else:
        b=StudentForm()
    return render(request,'basic_element.html',{'form':b})

def table(request):
    b=Student.objects.all()
    return render(request,'basic_tables.html',{'form':b})

def blogtable(request):
    b=Blog.objects.all()
    return render(request,'blogtable.html',{'b':b})

def insert(request):
    b=Blog.objects.all()
    if request.method=='POST':
        b=BlogForm(request.POST,request.FILES)
        print("++++++",b)
        if b.is_valid():
            try:
                upload(request.FILES['image'])
                b.save()
                return redirect('/insert/')
            except:
                print("++++++",sys.exc_info())

        else:
            pass
    else:
        form=BlogForm()
    return render(request,'insert.html')

def edit(request,id):
    b=Student.objects.get(id=id)
    return render(request,'edit.html',{'b':b})

def delete(request,id):
    b=Student.objects.get(id=id)
    b.delete()
    return redirect('/table/')


def update(request, id):
    b = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=b)
    if form.is_valid():
        form.save()
        return redirect('/table/')
    return render(request,'edit.html',{'form':form,"b":b})

def blogedit(request,id):
    b=Blog.objects.get(id=id)
    return render(request,'blogedit.html',{'b':b})

def blogupdate(request,id):
    b=Blog.objects.get(id=id)
    form=BlogForm(request.POST,request.FILES,instance=b)
    if form.is_valid():
        try:
            upload(request.FILES['image'])
            form.save()
            return redirect('/blogtable/')
        except:
            print("++++++",sys.exc_info())
    else:
        pass
    return render(request,'blogedit.html',{'form':form,'b':b})

def blogdelete(request,id):
    b=Blog.objects.get(id=id)
    b.delete()
    return redirect('/blogtable/')

def product(request):
    b=Blog.objects.all()
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        print('-------------', form)
        if form.is_valid():
            try:
                upload(request.FILES['pimage'])
                form.save()
                print('-----', form)
                return redirect("/product/")
            except:
                print("++++",sys.exc_info())
        else:
            pass
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form':form,'b':b})

def product_table(request):
    b=Product.objects.all()
    return render(request,'product_table.html',{'b':b})

def product_delete(request,id):
    b=Product.objects.get(id=id)
    b.delete()
    return redirect('/product_table/')

def product_edit(request,id):
    p=Blog.objects.all()
    b=Product.objects.get(id=id)
    return render(request,'product_edit.html',{'b':b,'p':p})

def product_update(request,id):
    b=Product.objects.get(id=id)
    p=Blog.objects.all()
    form=ProductForm(request.POST,request.FILES,instance=b)
    print("++++",form)
    if form.is_valid():
        try:
            upload(request.FILES['pimage'])
            form.save()
            print('+++++',form)
            return redirect('/product_table/')
        except:
            print('+++++',sys.exc_info())
    else:
        pass
    return render(request,'product_edit.html',{'form':form,'b':b,"p":p})


def gallary_add(request):
    b=Product.objects.all()
    if request.method=='POST':
        form=gallaryForm(request.POST,request.FILES)
        print('-------------', form)
        if form.is_valid():
            try:
                upload(request.FILES['image'])
                form.save()
                print('-----', form)
                return redirect("/gallary/")
            except:
                print("++++",sys.exc_info())
        else:
            pass
    else:
        form = gallaryForm()
    return render(request, 'gallary.html', {'form':form,'b':b})

def gallary_table(request):
    a = gallary.objects.all()
    return render(request,'gallary_table.html',{'a':a})
