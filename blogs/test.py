from unicodedata import category
from django.test import TestCase
from blogs.models import Post, Category
from django.contrib.auth.models import User

class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create(username='hossam1997', password='admin')
        test_post = Post.objects.create(category_id=1, title='testing title', content='testing content', slug='testing_title', author_id=1)
    
    def test_posting(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        title = f'{post.title}'
        content = f'{post.content}'
        slug = f'{post.slug}'
        author = f'{post.author}'


        self.assertEqual(title, 'testing title')
        self.assertEqual(content, 'testing content')
        self.assertEqual(author, 'hossam1997')
        self.assertEqual(slug, 'testing_title')
        self.assertEqual(str(cat), 'django')
        self.assertEqual(str(post), 'testing title')
