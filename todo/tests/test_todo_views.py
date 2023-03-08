from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse

from todo.models import ToDoItem


class ToDoListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    @classmethod
    def tearDown(cls):
        ToDoItem.objects.all().delete()

    def test_call_todo_list_view(self):
        response = self.client.get(reverse("todo:todo_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_call_todo_detail_view(self):
        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("todo:todo_detail"))

        response = self.client.get(
            reverse(
                "todo:todo_detail",
                kwargs={
                    "pk": 1,
                },
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_call_todo_create_view(self):
        response = self.client.get(reverse("todo:todo_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_create.html")

    def test_todo_create_view_post(self):
        response = self.client.post(
            reverse("todo:todo_create"),
            {
                "title": "Last ToDo Item",
                "status": "OPN",
                "priority": "N",
            },
        )
        self.assertEqual(response.url, reverse("todo:todo_list"))
