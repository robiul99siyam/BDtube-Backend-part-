import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import netfiex_app.routing as router


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netfiex_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        router.websocket_urlpatterns
    )
})
