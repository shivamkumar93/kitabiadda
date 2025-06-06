from django.shortcuts import render

# Create your views here.

def header(request):
    return render(request, 'public-panel/header.html')

def footer(request):
    return render(request, 'public-panel/footer.html')