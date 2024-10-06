from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

chat_rooms = {'rooms': []}

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    global chat_rooms
    if room_name != 'favicon.ico' and not room_name in chat_rooms:
        rooms = chat_rooms['rooms']
        rooms.append(room_name)
    return render(request, 'room.html', {'room_name': room_name})

class RoomSerializer(serializers.Serializer):
    rooms = serializers.ListField()

class RoomView(APIView):
    def get(self, request):
        global chat_rooms
        serializer = RoomSerializer(data=chat_rooms)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data)
