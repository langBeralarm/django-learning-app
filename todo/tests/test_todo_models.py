from django.test import TestCase

from todo.models import ToDoItem


class ToDoItemTestCase(TestCase):
    def test_get_todos(self):
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)
