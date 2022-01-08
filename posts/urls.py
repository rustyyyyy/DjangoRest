from django.urls import path
from .views import (
    post_list_and_create, load_post_data_view
)

app_name = 'posts'


urlpatterns = [
    path('',post_list_and_create,name="posts"),
    path('data/<int:num_posts>/',load_post_data_view,name="posts-data")
]