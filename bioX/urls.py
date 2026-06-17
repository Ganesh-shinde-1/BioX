
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import app


urlpatterns = [
    path('randomUser/', admin.site.urls),
    path('', include('app.urls')),
    path('tinymce/', include('tinymce.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




handler400 = 'app.views.error_400'
handler403 = 'app.views.error_403'
handler404 = 'app.views.error_404'
handler500 = 'app.views.error_500'


