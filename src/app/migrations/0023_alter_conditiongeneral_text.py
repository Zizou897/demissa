# Generated by Django 4.1.1 on 2023-04-14 11:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_conditiongeneral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditiongeneral',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
