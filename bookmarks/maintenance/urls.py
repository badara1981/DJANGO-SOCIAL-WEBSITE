from django.urls import path
from django.views.generic.edit import DeleteView
from .views import EditRoom, ListAllRoom, NewRoom, DeleteRoom

app_name = 'maint'
urlpatterns = [
    path('', ListAllRoom.as_view(), name='index'),
    path('new/room/', NewRoom.as_view(), name='new_room'),
    path('edit/<int:pk>/room/', EditRoom.as_view(), name='edit_room'),
    path('delete/<int:pk>/room/', DeleteRoom.as_view(), name='delete_room'),
]
