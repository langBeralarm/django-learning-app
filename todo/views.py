from django.shortcuts import render

from .models import ToDoItem


def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(
        request,
        "todo/todo_list.html",
        {
            "todos": todos,
        },
    )
