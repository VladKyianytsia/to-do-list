from django.test import TestCase, Client
from django.urls import reverse

from to_do_app.models import Tag, Task


class TestModel(TestCase):
    def test_tag_str_method(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)

    def test_task_str_method(self):
        task = Task.objects.create(
            content="Test",
        )
        self.assertEqual(str(task), task.content)


class TestToggleTaskCompletion(TestModel):
    def test_toggle_task_completion_when_done_is_false(self):
        self.client = Client()
        self.task = Task.objects.create(content="test")
        response = self.client.post(
            reverse(
                "to_do_app:toggle-task-completion",
                kwargs={"pk": self.task.id}
            )
        )
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.task.done)

    def test_toggle_task_completion_when_done_is_true(self):
        self.client = Client()
        self.task = Task.objects.create(content="test", done=True)
        response = self.client.post(
            reverse(
                "to_do_app:toggle-task-completion",
                kwargs={"pk": self.task.id}
            )
        )
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.task.done)
