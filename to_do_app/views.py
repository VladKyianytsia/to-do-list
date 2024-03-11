from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_app.forms import TaskForm
from to_do_app.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_app:task-list")


def toggle_task_completion(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    if task.done:
        task.done = False

    else:
        task.done = True

    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_app:task-list"))

