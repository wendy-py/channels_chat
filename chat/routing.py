from django.urls import re_path
from . import consumers

# channels routing is like django's urls
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.Chat.as_asgi()),
]
