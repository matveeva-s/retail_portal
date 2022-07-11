from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urls = [
    path('', include('recognizer_api.urls')),
    path('', include('assortment.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('auth/', include('auth_jwt.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)