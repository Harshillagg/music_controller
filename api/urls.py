from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path("rooms",RoomView.as_view()), #to get all the rooms
    path("create-room",CreateRoomView.as_view())
]