from dataclasses import field
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
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions, AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter

class PostWritePermission(BasePermission):
    message = 'Editing posts are only allowed for their respective author!'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         return Post.objects.all()

#     def get_object(self, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
    
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


class PostList(generics.ListAPIView):
    queryset = Post.get_published_posts.all()
    serializer_class = PostSerializer
    

# class PostDetail(generics.RetrieveAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostFilter(generics.ListAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     filter_backends =  [SearchFilter]
#     search_fields = ['^slug']
#     print('queryset: ', queryset)
#     print('filter: ', filter_backends)

    # '^' ==> Starts with
    # '=' ==> Exact matches
    # '@' ==> Full-text search (not supported by Django)
    # '$' ==> regex search 
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        id = self.kwargs.get('id') 
        print('get id: ', id)
        return Post.objects.get(id=id)

class CreatePost(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer_class = PostSerializer(data=request.data)
        print('Request data: ', request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            print('Serializer Data: ', serializer_class.data)
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class EditPost(generics.RetrieveUpdateAPIView):

    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.DestroyAPIView):

    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer