from django.contrib import admin
from .models import Car, Photo, Gallery, GalleryPhoto

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