from django.urls import path

from to_do_app.views import (
    TaskListView,
    TaskCreateView,
)

app_name = "to_do_app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create")
]
