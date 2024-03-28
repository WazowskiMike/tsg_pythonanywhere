from django.contrib import admin
from .models import Car, Photo, Gallery, GalleryPhoto, Order

class PhotoInline(admin.TabularInline):  
    model = Photo

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Photo)

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto

@admin.register(Gallery)
class GaleryAdmin(admin.ModelAdmin):
    inlines = [GalleryPhotoInline]  # Регистрация модели Gallery без дополнительных настроек

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'name', 'phone', 'email')  # Определяем, какие поля будут отображаться в списке заказов