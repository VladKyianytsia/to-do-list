from django.shortcuts import render
from django.views import generic

from to_do_app.models import Task


class TaskListView(generic.ListView):
    model = Task
