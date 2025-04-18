from django.urls import path
from .views import(
    posts_list_and_create,
    load_posts_data_view,
    like_unlike_post,
    post_detail,
    post_detail_data_view,
    delete_post,
    update_post,
    image_upload_view,

)
app_name = 'posts'

urlpatterns = [
    path('', posts_list_and_create, name='main-board'),
    path('like-unlike/', like_unlike_post, name='like-unlike'),
    path('upload/', image_upload_view, name='image-upload'),
    path('<pk>/', post_detail, name='post-detail'),
    path('<pk>/update/', update_post, name='post-update'),
    path('<pk>/delete/', delete_post, name='post-delete'),
    path('data/<int:num_posts>/', load_posts_data_view, name='posts-data'),
    path('<pk>/data/', post_detail_data_view, name='post-detail-data'),

]