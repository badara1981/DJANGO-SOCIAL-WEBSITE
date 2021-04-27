from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Rooms, Problem
from .forms import NewProblemForm


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


class ListAllProblems(ListView):
    template_name = 'maintenance/problems.html'
    context_object_name = 'problems'
    model = Problem
    fields = '__all__'

class EditProblem(UpdateView):
    template_name = 'maintenance/problem_edit.html'
    model = Problem
    fields = ('message', 'solve')

    def get_success_url(self) -> str:
        return reverse('maint:view_problems')

def new_problem(request):
    context = {}
    form = NewProblemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewProblemForm()
        return redirect('maint:view_problems')
    context['form'] = form
    return render(request, 'maintenance/new_problem.html', context)
