from django.shortcuts import render
from django.views import generic

from to_do_app.forms import TaskForm
from to_do_app.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
