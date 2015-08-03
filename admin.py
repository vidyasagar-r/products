from django.contrib import admin
from .models import Category, Products, User, Basket
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products)
admin.site.register(User)
admin.site.register(Basket)