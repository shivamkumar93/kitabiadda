from django.shortcuts import render
from kitab.models import *

# Create your views here.


def home(request):
    return render(request, "public-panel/home.html")

def header(request):
    data = {}
    data['categories'] = Category.objects.all()
    return render(request, 'public-panel/header.html', data)

def footer(request):
    return render(request, 'public-panel/footer.html')