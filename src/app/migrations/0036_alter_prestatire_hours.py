# Generated by Django 4.1.1 on 2023-05-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_prestatire_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestatire',
            name='hours',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
