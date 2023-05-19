from django.contrib import admin

from .models import Stocks, Services


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'created_at')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'created_at')
