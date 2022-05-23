from lib2to3.pgen2 import token
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import CreateCustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class CreateCustomUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateCustomUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TokenBlackListView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token_to_be_blacklisted = RefreshToken(refresh_token)
            token_to_be_blacklisted.blacklist()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


