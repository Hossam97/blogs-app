from pyexpat import model
from statistics import mode
from django import views
from django.shortcuts import get_object_or_404
from rest_framework import generics
from accounts.models import CustomUser
from blogs.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions, AllowAny

class PostWritePermission(BasePermission):
    message = 'Editing posts are only allowed for their respective author!'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def get_object(self, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    
# class PostList(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#     queryset = Post.get_published_posts.all()

#     def list(self, request):
#         serializer = PostSerializer(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.get_published_posts.all()
#     serializer_class = PostSerializer
#     pass

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostWritePermission):
#     permission_classes = [PostWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pass