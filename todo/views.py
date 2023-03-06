from django.views import generic

from .models import ToDoItem


class ToDoListView(generic.ListView):
    model = ToDoItem
    queryset = ToDoItem.objects.all()
    context_object_name = "todos"
    template_name = "todo/todo_list.html"


class ToDoDetailView(generic.DetailView):
    model = ToDoItem
    queryset = ToDoItem.objects.all()
    context_object_name = "todo"
    template_name = "todo/todo_detail.html"
