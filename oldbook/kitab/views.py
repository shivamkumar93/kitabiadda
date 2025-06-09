from django.shortcuts import render, redirect
from kitab.models import *
from django.contrib.auth import authenticate, login

# Create your views here.

# pubic panel views
def home(request):
    data = {}
    data['categories'] = Category.objects.all()
    return render(request, "public-panel/home.html", data)

def header(request):
    data = {}
    data['categories'] = Category.objects.all()
    return render(request, 'public-panel/header.html', data)

def footer(request):
    return render(request, 'public-panel/footer.html')

# user panel views

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            (request, "invalid username or password")
    return render(request, 'user-panel/login.html')
#admin panel views