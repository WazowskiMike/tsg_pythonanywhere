# Generated by Django 5.0.3 on 2024-03-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tsg_website", "0002_car_formatted_price_alter_car_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="photo",
            new_name="photo1",
        ),
        migrations.AddField(
            model_name="car",
            name="photo2",
            field=models.ImageField(blank=True, null=True, upload_to="media"),
        ),
        migrations.AddField(
            model_name="car",
            name="photo3",
            field=models.ImageField(blank=True, null=True, upload_to="media"),
        ),
        migrations.AddField(
            model_name="car",
            name="photo4",
            field=models.ImageField(blank=True, null=True, upload_to="media"),
        ),
        migrations.AddField(
            model_name="car",
            name="photo5",
            field=models.ImageField(blank=True, null=True, upload_to="media"),
        ),
    ]
