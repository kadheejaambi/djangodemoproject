from django.shortcuts import render,redirect
from app1.models import Movie
# Create your views here.
def home(request):
    m=Movie.objects.all()
    context={'movie':m}
    return render(request,'home.html',context)
def addmovies(request):
    if(request.method=="POST"):
        t=request.POST['t']
        d=request.POST['d']
        l=request.POST['l']
        y=request.POST['y']
        i=request.FILES['i']
        m=Movie.objects.create(title=t,desc=d,language=l,year=y,image=i)
        m.save()
        return redirect('home')

    return render(request,'addmovies.html')

def details(request,p):
    m = Movie.objects.get(id=p)
    context = {'movie': m}
    return render(request, 'details.html', context)
def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return redirect('home')
def update(request,p):
    m = Movie.objects.get(id=p)
    if request.method == "POST":  # After submitting the form
        m.title = request.POST['t']  # Title
        m.desc = request.POST['d']  # Description
        m.language = request.POST['l']  # Language
        m.year = request.POST['y']  # Year

        # Handle image upload
        if request.FILES.get('i'):
            m.image = request.FILES['i']

        m.save()  # Save the updated movie
        return redirect('movie:home')

    context = {'movie': m}
    return render(request, 'update.html', context)



