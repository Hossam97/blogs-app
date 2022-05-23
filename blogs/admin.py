from csv import list_dialects
from pdb import post_mortem
from django.contrib import admin
from blogs.models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'slug', 'content', 'author', 'status', 'published']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']