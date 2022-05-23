from django.urls import path
from .views import CreateCustomUser, TokenBlackListView


app_name = 'accounts'

urlpatterns = [
    path('register/', CreateCustomUser.as_view(), name="register_user"),
    path('logout/blacklist/', TokenBlackListView.as_view(), name='blacklist_token'),
]
