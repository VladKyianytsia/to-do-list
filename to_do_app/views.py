from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_app.forms import TaskForm
from to_do_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 4


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


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_app:tag-list")
