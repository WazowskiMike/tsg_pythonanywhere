from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('catalog/', views.catalog, name='catalog'),
    path('gallery/', views.gallery, name='gallery'),
    path('order/<str:car_name>/', views.order_page, name='order_page'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('details/<int:id>/', views.details, name='details'),
]
