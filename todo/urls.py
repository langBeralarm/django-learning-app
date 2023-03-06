from django.urls import path

from .views import ToDoDetailView, ToDoListView

app_name = "todo"

urlpatterns = [
    path("", ToDoListView.as_view(), name="todo_list"),
    path("<int:pk>/detail", ToDoDetailView.as_view(), name="todo_detail"),
]
