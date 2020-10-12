from django.contrib import admin
from brew.models import *

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('client', 'provider', 'estimated')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('key', 'provider', 'value', 'quantity')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'photo')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'lat', 'lon', 'name', 'description', 'address', 'photo', 'phone', 'side', 'rank')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text')

admin.site.site_header = "Delivery Dashboard"
