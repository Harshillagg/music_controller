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

#view to create a room
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    #post method to create a room
    def post(self, request, format=None):

        #check if session exists
        if not self.request.session.exists(self.request.session.session_key): 
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)

        #check if serializer is valid
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')    
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)

            #check if room exists for the session_key
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip  
                room.save(update_fields=['guest_can_pause', 'votes_to_skip']) #update the fields
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip) #else create a new room
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)