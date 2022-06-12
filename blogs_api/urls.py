from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, CreatePost, EditPost, DeletePost


app_name = 'blogs_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [
    path('', PostList.as_view(), name='create_list'),
    path('posts/<int:id>/', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', CreatePost.as_view(), name='create_post'),
    path('posts/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

]
