"""
ASGI config for mywebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
from channels.routing import ProtocolTypeRouter,URLRouter

from channels.auth import AuthMiddlewareStack
import chat.routing



application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(# web socket need auth middleware,session middleware,cookie middle
        #ware to work,so these 3 are provied in authmiddleware stack
        URLRouter(
            chat.routing.websocket_urlpatterns
        )

    )
})
