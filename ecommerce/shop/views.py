from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request,'categories.html')
def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,i):
    c=Category.objects.get(id=i)
    p=Product.objects.filter(category=c)
    context={'cat':c,'pro':p}
    return render(request,'products.html',context)
def productdetail(request,i):
    p = Product.objects.get(id=i)
    context={'pro':p}
    return render(request, 'detail.html',context)

from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
# Create your views here.
def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
        else:
            return HttpResponse("password should be same")

        return redirect('shop:categories')

    return render(request,'register.html')





def user_login(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)  #cheecks whether the dtails entered by user is correct or nor
        if user:     # if user already exist
            login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:categories')


# views.py
from django.shortcuts import render, redirect
from .models import Category
from django.contrib import messages


def addcategories(request):
    if (request.method == 'POST'):

        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']

        c=Category.objects.create(name=n, image=i, desc=d)
        c.save()

        return redirect('shop:categories')

    return render(request, 'addcategories.html')


def  addproducts(request):
    if(request.method == 'POST'):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        p = request.POST['p']
        s = request.POST['s']
        c = request.POST['c']  #category name
        cat=Category.objects.get(name=c)   #retreive a category record matching with that name


        m=Product.objects.create(name=n, image=i, desc=d,price=p,stock=s,category=cat) #here category is foreign key feild

        m.save()

        return redirect('shop:categories')

    return render(request, 'addproducts.html')

def addstock(request,i):
        p = Product.objects.get(id=i)
        if (request.method == "POST"):
            p.stock = request.POST['n']
            p.save()
            return redirect('shop:detail', i)



        context = {'pro': p}
        return render(request, 'addstock.html', context)


def addtocart(request):
    return render(request,'addtocart.html')


