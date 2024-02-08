from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('aulas.urls')),
    path('api/v1/', include('reservations.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('matching_aulas.urls')),
    path('api/v1/', include('allowed_emails.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
