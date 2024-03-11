from django.urls import path

from to_do_app.views import TaskListView

app_name = "to_do_app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list")
]
