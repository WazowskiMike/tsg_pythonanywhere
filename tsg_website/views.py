from django.shortcuts import render

def index(request):
    return render(request, 'tsg_website/index.html')

def catalog(request):
    return render(request, 'tsg_website/catalog.html')