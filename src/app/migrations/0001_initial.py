# Generated by Django 4.1.1 on 2022-11-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='img_web')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Info du site',
                'verbose_name_plural': 'Infos du site',
            },
        ),
    ]