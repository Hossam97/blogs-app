from turtle import Turtle, title
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
# Create your models here.


def upload_to(instsance, filename):
    return f'posts/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    def __str__(self):
            return self.title

    

    class GetPublishedPosts(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        

    options=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, null=True, blank=True )
    image = models.ImageField(upload_to=upload_to, default='posts/default.png', null=True, blank=True)
    status = models.CharField(max_length=50,choices=options, default='published')
    published = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    get_published_posts = GetPublishedPosts()


    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
          


