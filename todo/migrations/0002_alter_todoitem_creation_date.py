# Generated by Django 4.1.7 on 2023-03-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
