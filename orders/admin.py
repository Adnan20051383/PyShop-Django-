from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total')


admin.site.register(Order, OrderAdmin)
