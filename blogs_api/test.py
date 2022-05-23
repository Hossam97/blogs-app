from django.test import TestCase
from blogs.models import Post, Category
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

class TestPostAPI(APITestCase):
    def test_posts_list(self):
        url = reverse('blogs_api:create_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)