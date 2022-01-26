from django.urls import path, include
from . import views

urlpatterns =[

    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_view,name="login_user"),

    path('',views.home, name="home"),
    path('product/',views.home, name="home"),
    path('add-product',views.createProduct, name="add-product"),
    path('edit-product/<str:pk>',views.editProduct, name="edit-product"),
    path('delete-product/<str:pk>',views.deleteProduct, name="delete-product"),

    path('brands/',views.brand, name="brands"),
    path('edit-brands/<str:pk>',views.editBrand, name="edit-brands"),
    path('add-brand/',views.addBrand, name="add-brand"),
    path('delete-brands/<str:pk>',views.deleteBrand, name="delete-brands"),
]
