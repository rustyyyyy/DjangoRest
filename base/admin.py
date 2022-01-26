from django.contrib import admin

# Register your models here.
from .models import product,Brand

# registerlist = ['product','Brand']

# admin.site.register(product)
admin.site.register(Brand)


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','date']
    list_filter = ('price',)