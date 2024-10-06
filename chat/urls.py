from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get_rooms/', views.RoomView.as_view(), name='room_names'),
    path('<str:room_name>/', views.room, name='room'),
]
