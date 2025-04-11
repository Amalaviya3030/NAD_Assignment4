from django.urls import path
from .views import(
    posts_list_and_create,
    load_posts_data_view,
    like_unlike_post,
    post_detail,
    post_detail_data_view,

)
app_name = 'posts'

urlpatterns = [
    path('', posts_list_and_create, name='main-board'),
    path('like-unlike/', like_unlike_post, name='like-unlike'),
    path('<pk>/', post_detail, name='post-detail'),
    path('data/<int:num_posts>/', load_posts_data_view, name='posts-data'),
    path('<pk>/data/', post_detail_data_view, name='post-detail-data'),

]