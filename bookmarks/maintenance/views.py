from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Rooms, Problem


class ListAllRoom(ListView):
    template_name = 'maintenance/all_room.html'
    context_object_name = 'rooms'
    model = Rooms
    fields = '__all__'


class EditRoom(UpdateView):
    template_name = 'maintenance/edit_room.html'
    model = Rooms
    fields = '__all__'

    def get_success_url(self):
        return reverse('maint:index')


class NewRoom(CreateView):
    template_name = 'maintenance/new_room.html'
    model = Rooms
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse('maint:index')


class DeleteRoom(DeleteView):
    template_name = 'maintenance/delete_room.html'
    context_object_name = 'rooms'
    model = Rooms
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse('maint:index')
