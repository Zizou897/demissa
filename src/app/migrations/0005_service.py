# Generated by Django 4.1.1 on 2022-11-06 23:53

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_about_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='img_service')),
                ('picture1', models.FileField(upload_to='img_service')),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('service_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
