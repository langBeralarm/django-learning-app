# Generated by Django 4.1.7 on 2023-03-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                ("creation_date", models.DateTimeField()),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPN", "Open"),
                            ("CLD", "Closed"),
                            ("WIP", "in Progess"),
                        ],
                        default="OPN",
                        max_length=3,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("L", "Low"),
                            ("N", "Normal"),
                            ("H", "High"),
                            ("U", "Urgent"),
                        ],
                        default="N",
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]
