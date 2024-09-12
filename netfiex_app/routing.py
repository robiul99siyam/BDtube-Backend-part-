from django.urls import path
from .consumers import MyNotification


websocket_urlpatterns = [
    path("ws/sc/",MyNotification.as_asgi())
]