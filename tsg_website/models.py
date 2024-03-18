from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    formatted_price = models.CharField(max_length=20, blank=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.formatted_price = intcomma(self.price)
        super().save(*args, **kwargs)

class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return f"Photo of {self.car.name}"
