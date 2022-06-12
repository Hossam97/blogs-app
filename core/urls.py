from webbrowser import get
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blogs.urls', namespace='blogs')),
    path('api/', include('blogs_api.urls', namespace='blogs_api')),
    path('api/user/', include('accounts.urls', namespace='accounts')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # simple jwt authentication:
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    path('docs/', include_docs_urls(title='BlogAPI')),
    
    path('schema/', get_schema_view(
        title='BlogAPI',
        description='API for the BlogAPI',
        version='1.0.0', 
        permission_classes=[AllowAny]
    ), name='openapi-schema')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
