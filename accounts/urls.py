from django.urls import path
from .views import CreateCustomUser


app_name = 'accounts'

urlpatterns = [
    path('register/', CreateCustomUser.as_view(), name="register_user"),
]
