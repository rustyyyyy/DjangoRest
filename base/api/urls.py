from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('api/products/',views.productList, name="productList"),
    path('api/products/<str:pk>',views.productDetail, name="products"),
    path('api/products-create/',views.productSave, name="products-create"),
    path('api/products-update/<str:pk>',views.productUpdate, name="products-update"),
    path('api/products-delete/<str:pk>',views.productDelete, name="products-delete"),
]

