from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer,CreateRoomSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

#view to show all the rooms and their details.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        pass