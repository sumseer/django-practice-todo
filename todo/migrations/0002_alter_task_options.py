# Generated by Django 5.1.3 on 2024-11-27 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_done", "-created_at"]},
        ),
    ]
