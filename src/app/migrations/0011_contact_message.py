# Generated by Django 4.1.1 on 2023-02-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0010_remove_contact_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="message",
            field=models.TextField(default="veuillez nous contacter"),
        ),
    ]