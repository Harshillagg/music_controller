from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics

# Create your views here.

#view for creating room . shows all the rooms and their details.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
