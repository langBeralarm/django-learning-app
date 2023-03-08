from django.test import TestCase

from todo.forms import ToDoCreateForm
from todo.models import ToDoItem
from todo.views import ToDoDeleteView


class ToDoItemTestCase(TestCase):
    @classmethod
    def tearDown(cls):
        ToDoItem.objects.all().delete()

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

    def test_delete_todo(self):
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

        ToDoItem.objects.create(title="ToDo Item")
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 1)

        ToDoItem.objects.all().delete()
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 0)

    def test_todo_delete_form(self):
        ToDoItem.objects.create(title="ToDo Item")
        todos = ToDoItem.objects.all().count()
        self.assertEqual(todos, 1)

        form_data = {
            "Confirm": True,
        }
        form = ToDoDeleteView.form_class(data=form_data)
        self.assertTrue(form.is_valid())
