from django.views import generic

from .models import ToDoItem


class ToDoList(generic.ListView):
    model = ToDoItem
    queryset = ToDoItem.objects.all()
    context_object_name = "todos"
    template_name = "todo/todo_list.html"
