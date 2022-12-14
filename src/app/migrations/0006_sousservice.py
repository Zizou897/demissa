# Generated by Django 4.1.1 on 2022-11-07 00:29

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='SousService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='img_service')),
                ('libele', models.TextField()),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('price', models.CharField(max_length=100)),
                ('sous_service_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_service', to='app.service')),
            ],
            options={
                'verbose_name': 'Sous Service',
                'verbose_name_plural': 'Sous Services',
            },
        ),
    ]
