from django.contrib import admin
from products.models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
