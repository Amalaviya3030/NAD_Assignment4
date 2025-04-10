from django.urls import path
from .views import(
    posts_list_and_create,
    load_posts_data_view,
    hello_world_view
)
app_name = 'posts'

urlpatterns = [
    path('', posts_list_and_create, name='main-board'),
    path('data/', load_posts_data_view, name='posts-data'),
    path('hello-world/', hello_world_view, name='hello-world'),
]