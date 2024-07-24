from django.urls import path

from products import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_product)
]