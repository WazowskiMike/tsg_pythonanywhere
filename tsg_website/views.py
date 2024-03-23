from django.shortcuts import render
from .models import Car
from django.db.models import Min, Max
from django.contrib.humanize.templatetags.humanize import intcomma

def index(request):
    return render(request, 'tsg_website/index.html')

def catalog(request):
    cars = Car.objects.all()
    user = request.user
    query = request.GET.get('search')
    min_price = cars.aggregate(Min('price'))['price__min'] or 0
    max_price = cars.aggregate(Max('price'))['price__max'] or 1000000
    min_mileage = Car.objects.aggregate(Min('mileage'))['mileage__min'] or 0
    max_mileage = Car.objects.aggregate(Max('mileage'))['mileage__max'] or 300000
    min_price_for_car = request.GET.get('priceMin')
    max_price_for_car = request.GET.get('priceMax')
    min_mileage_for_car = request.GET.get('mileageMin')
    max_mileage_for_car = request.GET.get('mileageMax')
    year = request.GET.get('year')
    make = request.GET.get('make')
    model = request.GET.get('model')
    body_color = request.GET.get('color')
    body_type = request.GET.get('body_type')
    transmission = request.GET.get('transmission')
    fuel_type = request.GET.get('fuel_type')
    years = cars.values_list('year_of_manufacture', flat=True).distinct().order_by('year_of_manufacture')
    makes = cars.values_list('make', flat=True).distinct().order_by('make')
    models = cars.values_list('model', flat=True).distinct().order_by('model')
    colors = cars.values_list('body_color', flat=True).distinct().order_by('body_color')
    body_types = cars.values_list('body_type', flat=True).distinct().order_by('body_type')
    transmissions = cars.values_list('transmission', flat=True).distinct().order_by('transmission')
    fuel_types = cars.values_list('fuel_type', flat=True).distinct().order_by('fuel_type')
    
    if query:
        cars = cars.filter(name__icontains=query)
    
    if min_price_for_car:
        cars = cars.filter(price__gte=min_price_for_car)
    if max_price_for_car:
        cars = cars.filter(price__lte=max_price_for_car)
    
    if min_mileage_for_car:
        cars = cars.filter(mileage__gte=min_mileage_for_car)
    if max_mileage_for_car:
        cars = cars.filter(mileage__lte=max_mileage_for_car)

    if year:
        years = request.GET.getlist('year')
        cars = cars.filter(year_of_manufacture__in=years)

    if make:
        makes = request.GET.getlist('make')
        cars = cars.filter(make__in=makes)

    if model:
        models = request.GET.getlist('model')
        cars = cars.filter(model__in=models)

    if body_color:
        colors = request.GET.getlist('color')
        cars = cars.filter(body_color__in=colors)

    if body_type and body_type != 'Any':
        body_types = request.GET.getlist('body_type')
        cars = cars.filter(body_type__in=body_types)

    if transmission and transmission != 'Any':
        transmissions = request.GET.getlist('transmission')
        cars = cars.filter(transmission__in=transmissions)

    if fuel_type and fuel_type != 'Any':
        fuel_types = request.GET.getlist('fuel_type')
        cars = cars.filter(fuel_type__in=fuel_types)

    context = {
        'cars': cars,
        'user': user,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'min_mileage': min_mileage,
        'max_mileage': max_mileage,
        'years': years,
        'makes': makes,
        'models': models,
        'colors': colors,
        'body_types': body_types,
        'transmissions': transmissions,
        'fuel_types': fuel_types,
    }
    return render(request, 'tsg_website/catalog.html', context=context)