from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class ToDoListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_call_todo_list_view(self):
        response = self.client.get(reverse("todo:todo_list"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("todo:todo_list"))
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
