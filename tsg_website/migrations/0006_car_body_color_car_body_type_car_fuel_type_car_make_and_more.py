# Generated by Django 5.0.3 on 2024-03-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsg_website', '0005_car_is_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_color',
            field=models.CharField(default='Unknown', max_length=50, verbose_name='Body Color'),
        ),
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('suv', 'SUV'), ('wagon', 'Wagon'), ('coupe', 'Coupe'), ('convertible', 'Convertible')], default='Unknown', max_length=20, verbose_name='Body Type'),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('electric', 'Electric')], default='Unknown', max_length=20, verbose_name='Fuel Type'),
        ),
        migrations.AddField(
            model_name='car',
            name='make',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Make'),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=0, verbose_name='Mileage'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='Unknown', max_length=20, verbose_name='Transmission'),
        ),
        migrations.AddField(
            model_name='car',
            name='year_of_manufacture',
            field=models.IntegerField(default=0, verbose_name='Year of Manufacture'),
        ),
    ]