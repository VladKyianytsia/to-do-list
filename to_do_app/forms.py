from django import forms

from to_do_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date"}
            ),
            "tags": forms.CheckboxSelectMultiple()
        }
