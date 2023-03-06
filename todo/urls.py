from django.urls import path

from .views import ToDoList

app_name = "todo"

urlpatterns = [
    path("", ToDoList.as_view(), name="todo_list"),
]
