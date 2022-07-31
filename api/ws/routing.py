from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/order/<str:username>/', consumers.OrderConsumer),
    # path('ws/<slug:room_name>/', consumers.MessageConsumer),
]
