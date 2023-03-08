from django.forms import DateInput, ModelForm

from .models import ToDoItem


class ToDoForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["title", "description", "due_date", "status", "priority"]
        widgets = {
            "due_date": DateInput(
                attrs={
                    "type": "date",
                }
            )
        }
