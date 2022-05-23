from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import TokenBlackListView

from accounts.views import CreateCustomUser

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blogs.urls', namespace='blogs')),
    path('api/', include('blogs_api.urls', namespace='blogs_api')),
    path('api/user/', include('accounts.urls', namespace='accounts')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

]
