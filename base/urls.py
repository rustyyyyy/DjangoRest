from django.urls import path, include
from . import views

urlpatterns =[

    path('',views.home, name="home"),
    path('add-product',views.createProduct, name="add-product"),
    path('edit-product/<str:pk>',views.editProduct, name="edit-product"),
    path('delete-product/<str:pk>',views.deleteProduct, name="delete-product"),
]
