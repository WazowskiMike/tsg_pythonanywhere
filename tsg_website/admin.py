from django.contrib import admin
from .models import Car, Photo

class PhotoInline(admin.TabularInline):  
    model = Photo

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Photo)
