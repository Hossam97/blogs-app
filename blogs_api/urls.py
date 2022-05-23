# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList


app_name = 'blogs_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     path('', PostList.as_view(), name='create_list'),
#     path('<int:pk>/', PostDetail.as_view(), name='create_post_detail'),
    
# ]
