from django.contrib import admin
from assets.views import dashboard
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # User Registration URLs
    path('users/', include('users.urls')),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Movies URLs
    path('', include('movies.urls')),

      path(
        'api/',
        include('movies.api_urls')
    ),

       path(
        'api/token/',
        TokenObtainPairView.as_view(),
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
    ),

      path(
        'api/',
        include('assets.api_urls')
    ),

    path(
    "dashboard/",dashboard
    ),

    path('api/', include('assets.urls')),
]

# Media files
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )