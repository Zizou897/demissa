# Generated by Django 4.1.1 on 2023-02-18 09:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="message",
        ),
    ]