from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('questionnaire.urls', namespace='questionnaire')),
    path('about/', include('about.urls', namespace='about')),
    path('likes/', include('likes.urls', namespace='likes')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
