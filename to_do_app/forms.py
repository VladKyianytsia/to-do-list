from django import forms

from to_do_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"}
        ),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )
