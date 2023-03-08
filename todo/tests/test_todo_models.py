from django.test import TestCase

from todo.models import ToDoItem


class ToDoItemTestCase(TestCase):
    def test_get_todos(self):
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

    def test_create_todo(self):
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

        todo = ToDoItem.objects.create(title="ToDo Item")
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 1)

        self.assertEqual(todo.title, "ToDo Item")
        self.assertEqual(todo.status, "OPN")
        self.assertEqual(todo.priority, "N")
