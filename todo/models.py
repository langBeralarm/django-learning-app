from django.db import models
from django.utils.translation import gettext_lazy as _


class ToDoItem(models.Model):
    """
    ToDoItem is an item to store ToDo's with a title, optional description,
    creation date and optional due date.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    class ToDoStatus(models.TextChoices):
        OPEN = "OPN", _("Open")
        CLOSED = "CLD", _("Closed")
        IN_PROGRESS = "WIP", _("in Progess")

    status = models.CharField(
        max_length=3,
        choices=ToDoStatus.choices,
        default=ToDoStatus.OPEN,
    )

    class ToDoPriority(models.TextChoices):
        LOW = "L", _("Low")
        NORMAL = "N", _("Normal")
        HIGH = "H", _("High")
        URGENT = "U", _("Urgent")

    priority = models.CharField(
        max_length=1,
        choices=ToDoPriority.choices,
        default=ToDoPriority.NORMAL,
    )

    def __str__(self):
        return self.title
