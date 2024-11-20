from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']
        c=request.FILES['c']
        f=request.FILES['f']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)  #create a new record
        b.save() #save the record inside table book
        return view_books(request)
    return render(request,'add_books.html')
@login_required
def view_books(request):
    k=Book.objects.all()  #read all records from table
    context={'book':k}    # pass all data from views to html file.context is dictiony type

    return render(request,'view_books.html',context)

def detail(request,p):
    b=Book.objects.get(id=p)
    context={'book':b}
    return render(request, 'detail.html',context)
def edit(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):  # After submitting form
        b.title  = request.POST['t']
        b.author = request.POST['a']
        b.price = request.POST['p']
        b.pages = request.POST['pa']
        b.language = request.POST['l']
        if(request.FILES.get('c')==None):
            b.save()
        else:
            b.cover=request.FILES.get('c')
        if (request.FILES.get('f') == None):
            b.save()
        else:
            b.pdf = request.FILES.get('f')

        b.save()
        return redirect('books:view_books')

    context={'book':b}
    return render(request,'edit.html',context)

def delete(request,p):
    b = Book.objects.get(id=p)
    b.delete()
    return redirect('books:view_books')

from django.db.models import Q
def search(request):
    b=None   # initialised to none ...if there is no query then automatically none
    query=""
    if (request.method == "POST"):  # after form submission
        query=request.POST['q']
        if query:
            b = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


    return render(request, 'search.html',{'books':b,'query':query})



