from django.shortcuts import redirect, render
from django.views import generic

from .forms import ToDoCreateForm
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


class ToDoCreateView(generic.CreateView):
    model = ToDoItem
    form_class = ToDoCreateForm
    template_name = "todo/todo_create.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            form = ToDoCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("todo:todo_list")
        else:
            form = ToDoCreateForm()
        return render(
            request,
            "todo/todo_create.html",
            {
                "form": form,
            },
        )
