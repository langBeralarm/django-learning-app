from django.test import Client, TestCase
from django.urls import reverse


class ToDoListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_get_todo_list_view(self):
        response = self.client.get(reverse("todo:todo_list"))
        self.assertEqual(response.status_code, 200)

    def test_call_todo_list_view(self):
        response = self.client.get(reverse("todo:todo_list"))
        self.assertTemplateUsed(response, "todo/todo_list.html")
