from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    formatted_price = models.CharField(max_length=20, blank=True)
    is_sold = models.BooleanField(default=False)
    year_of_manufacture = models.IntegerField(("Year of Manufacture"), default=0)
    make = models.CharField(("Make"), max_length=100, blank=True)
    model = models.CharField(("Model"), max_length=100, default="Unknown")
    mileage = models.IntegerField(("Mileage"), default=0)
    body_color = models.CharField(("Body Color"), max_length=50, default="Unknown")

    BODY_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
    ]
    body_type = models.CharField(("Body Type"), max_length=20, choices=BODY_TYPE_CHOICES, default="Unknown")

    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    transmission = models.CharField(("Transmission"), max_length=20, choices=TRANSMISSION_CHOICES, default="Unknown")

    FUEL_TYPE_CHOICES = [
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
    ]
    fuel_type = models.CharField(("Fuel Type"), max_length=20, choices=FUEL_TYPE_CHOICES, default="Unknown")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.formatted_price = intcomma(self.price)
        self.make = self.name.split(' ')[0]
        super().save(*args, **kwargs)

class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return f"Photo of {self.car.name}"
