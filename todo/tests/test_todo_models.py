from django.test import TestCase

from todo.forms import ToDoCreateForm
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

    def test_todo_create_form(self):
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

        form_data = {
            "title": "ToDo Test",
            "status": "OPN",
            "priority": "N",
        }
        form = ToDoCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

        form.save()

        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 1)
