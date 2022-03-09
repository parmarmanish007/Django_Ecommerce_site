from django.shortcuts import render,redirect
from.models import Student,Blog,Product
from.form import StudentForm,BlogForm,ProductForm
from.function import upload

# Create your views here.
def index(request):
    return render(request,'index.html')

def basic_element(request):
    if request.method=='POST':
        b=StudentForm(request.POST)
        print('++++++',b)
        if b.is_valid():
            b.save()
            return redirect('/basic_element/')
        else:
            pass
    else:
        form=StudentForm()
        return render(request,'basic_element.html')

def formtable(request):
    b=Student.objects.all()
    return render(request,'formtable.html',{'form':b})

def formedit(request,id):
    b=Student.objects.get(id=id)
    return render(request,'formedit.html',{'b':b})

def formupdate(request,id):
    b=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return redirect('/formtable/')
        return render(request,'formedit.html',{'form':form,"b":b})
def formdelete(request,id):
    b=Student.objects.get(id=id)
    b.delete()
    return redirect('/formtable/')

def blog_element(request):
    b=Blog.objects.all()
    if request.method=='POST':
        b=BlogForm(request.POST,request.FILES)
        print("++++",b)
        if b.is_valid():
            try:
                upload(request.FILES['image'])
                b.save()
                return redirect('/blog_element/')
            except:
                pass
        else:
            pass
    else:
        form=BlogForm()
        return render(request,'blog_element.html')

def blog_table(request):
    b=Blog.objects.all()
    return render(request,'blog_table.html',{'b':b})

def blog_edit(request,id):
    b=Blog.objects.get(id=id)
    return render(request,'blog_edit.html',{'b':b})

def blog_update(request,id):
    b=Blog.objects.get(id=id)
    if request.method=='POST':
        b=BlogForm(request.POST,request.FILES,instance=b)
        print("++++",b)
        if b.is_valid():
            try:
                upload(request.FILES['image'])
                b.save()
                return redirect('/blog_table/')
            except:
                pass
        else:
            pass
    else:
        return render(request,'blog_edit.html',{'b':b})

def blog_delete(request,id):
    b=Blog.objects.get(id=id)
    b.delete()
    return redirect('/blog_table/')

def product(request):
    b=Blog.objects.all()
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        print("++++",form)
        if form.is_valid():
            try:
                upload(request.FILES['pimage'])
                form.save()
                return redirect('/product/')
            except:
                pass
        else:
            pass
    else:
        form=ProductForm()
        return render(request,'product.html',{'form':form,'b':b})

def product_table(request):
    b=Product.objects.all()
    return render(request,'product_table.html',{'b':b})

def product_edit(request,id):
    b=Product.objects.get(id=id)
    p=Blog.objects.all()
    return render(request,'product_edit.html',{'b':b,'p':p})

def product_update(request,id):
    b=Product.objects.get(id=id)
    p=Blog.objects.all()
    form=ProductForm(request.POST,request.FILES,instance=b)
    print('++++',form)
    if form.is_valid():
        try:
            upload(request.FILES['pimage'])
            form.save()
            return redirect('/product_table/')
        except:
            pass
    else:
        pass
    return render(request,'product_edit.html',{'form':form,'b':b,"p":p})

def product_delete(request,id):
    b=Product.objects.get(id=id)
    b.delete()
    return redirect('/product_table/')