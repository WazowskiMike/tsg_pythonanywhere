from django.shortcuts import render, redirect
from .models import Car, Gallery
from django.db.models import Min, Max
from django.contrib.humanize.templatetags.humanize import intcomma
from .forms import OrderForm
import telebot

def index(request):
    try:
        gallery = Gallery.objects.get(pk=1)  # Получаем единственный экземпляр Gallery
        photos = gallery.gallery_photos.all()  # Получаем все связанные фотографии
    except Gallery.DoesNotExist:
        photos = []  # Если галерея не найдена, возвращаем пустой список
    return render(request, 'tsg_website/index.html', {'photos': photos})

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

def gallery(request):
    try:
        gallery = Gallery.objects.get(pk=1)  # Получаем единственный экземпляр Gallery
        photos = gallery.gallery_photos.all()  # Получаем все связанные фотографии
    except Gallery.DoesNotExist:
        photos = []  # Если галерея не найдена, возвращаем пустой список
    return render(request, 'tsg_website/gallery.html', {'photos': photos})

def order_page(request, car_name):
    # Здесь вы можете добавить логику для создания страницы заказа
    # Это может включать в себя форму заказа и другие данные, связанные с автомобилем
    return render(request, 'tsg_website/order_page.html', {'car_name': car_name})

TELEGRAM_BOT_TOKEN = '7161604572:AAHhX7XrIET7TdUJ3FvToul_KJqPJzDInTI'
# ID чата или пользователя, которому бот будет отправлять сообщения
TELEGRAM_CHAT_ID = '1108252918'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def submit_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            car_name = order.car_name
            name = order.name
            phone = order.phone
            email = order.email
            # Сообщение, которое будет отправлено через бота
            message = f'New order received for {car_name}. Name: {name}, Phone: {phone}, Email: {email}'
            # Отправка сообщения
            bot.send_message(TELEGRAM_CHAT_ID, message)

            return redirect('/catalog')
    else:
        initial_data = {'car_name': request.POST.get('car_name')}
        form = OrderForm(initial=initial_data)

    return render(request, 'tsg_website/order_page.html', {'form': form})