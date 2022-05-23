from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        username = username.lower()
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password, **other_fields):
        user = self.create_user(email, username, password, **other_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']
    
    def __str__(self):
        return self.username
