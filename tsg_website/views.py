from django.shortcuts import render
from .models import Car

def index(request):
    return render(request, 'tsg_website/index.html')

def catalog(request):
    cars = Car.objects.all()
    user = request.user
    context = {
        'cars':cars,
        'user':user
    }
    return render(request, 'tsg_website/catalog.html', context=context)