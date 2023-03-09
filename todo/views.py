from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ToDoForm
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
    form_class = ToDoForm
    template_name = "todo/todo_create.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            form = ToDoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("todo:todo_list")
        else:
            form = ToDoForm()
        return render(
            request,
            "todo/todo_create.html",
            {
                "form": form,
            },
        )


class ToDoDeleteView(generic.DeleteView):
    model = ToDoItem
    template_name = "todo/todo_delete.html"
    success_url = reverse_lazy("todo:todo_list")
    context_object_name = "todo"


class ToDoUpdateView(generic.UpdateView):
    model = ToDoItem
    form_class = ToDoForm
    template_name = "todo/todo_update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo:todo_list")

    # def get_object(self, queryset=None):
    #     return ToDoItem.objects.get(pk=self.kwargs["pk"])
