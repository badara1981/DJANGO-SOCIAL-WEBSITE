from django.urls import path
from django.views.generic.edit import DeleteView
from .views import EditRoom, ListAllRoom, NewRoom, DeleteRoom, ListAllProblems, EditProblem, new_problem

app_name = 'maint'
urlpatterns = [
    path('', ListAllRoom.as_view(), name='index'),
    path('new/room/', NewRoom.as_view(), name='new_room'),
    path('edit/<int:pk>/room/', EditRoom.as_view(), name='edit_room'),
    path('delete/<int:pk>/room/', DeleteRoom.as_view(), name='delete_room'),

    path('view-problems/', ListAllProblems.as_view(), name='view_problems'),
    path('new/problem/', new_problem, name='new_problem'),
    path('edit/<int:pk>/problem/', EditProblem.as_view(), name='edit_problem'),
]
