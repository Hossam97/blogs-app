from django.urls import path
from django.views.generic import TemplateView
from blogs_api.views import PostDetail

app_name='blogs'
urlpatterns = [
    path('', TemplateView.as_view(template_name="blogs/index.html")),
    # path('posts/<int:id>', PostDetail.as_view(), name='post_detail')
]
