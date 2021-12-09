from django.urls import path
from . import  viewsApi


urlpatterns =[
    path('api/products/',viewsApi.productList, name="productList"),
    path('api/products/<str:pk>',viewsApi.productDetail, name="products"),
    path('api/products-create/',viewsApi.productSave, name="products-create"),
    path('api/products-update/<str:pk>',viewsApi.productUpdate, name="products-update"),
    path('api/products-delete/<str:pk>',viewsApi.productDelete, name="products-delete"),
]
