from django.urls import path

from .views import ToDoDetail, ToDoList

app_name = "todo"

urlpatterns = [
    path("", ToDoList.as_view(), name="todo_list"),
    path("<int:pk>/detail", ToDoDetail.as_view(), name="todo_detail"),
]
