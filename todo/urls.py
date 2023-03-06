from django.urls import path

from .views import ToDoCreateView, ToDoDetailView, ToDoListView

app_name = "todo"

urlpatterns = [
    path("", ToDoListView.as_view(), name="todo_list"),
    path("create/", ToDoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/detail", ToDoDetailView.as_view(), name="todo_detail"),
]
