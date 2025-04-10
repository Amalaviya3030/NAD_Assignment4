from django.urls import path
from .views import(
    posts_list_and_create,
)
app_name = 'posts'

urlpatterns = [
    path('', posts_list_and_create, name='main'),
]