from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("netfiex/",include("netfiex_app.urls")),
    path("user/",include("user_auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ debug_toolbar_urls()
