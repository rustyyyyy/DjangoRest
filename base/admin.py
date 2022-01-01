from django.contrib import admin

# Register your models here.
from .models import product,Brand

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('brandname',)
    search_fields =['name']

admin.site.register(product,ProductAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display =('name','id',)

admin.site.register(Brand,BrandAdmin)

