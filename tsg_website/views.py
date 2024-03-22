from django.shortcuts import render
from .models import Car

def index(request):
    return render(request, 'tsg_website/index.html')

def catalog(request):
    cars = Car.objects.all()
    user = request.user
    query = request.GET.get('search')  # Получаем значение поискового запроса
    if query:  # Если запрос присутствует, фильтруем список машин
        cars = cars.filter(name__icontains=query)
    context = {
        'cars': cars,
        'user': user,
        'query': query  # Передаем значение запроса в контекст для отображения в шаблоне
    }
    return render(request, 'tsg_website/catalog.html', context=context)