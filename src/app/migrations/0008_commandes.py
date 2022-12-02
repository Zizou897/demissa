# Generated by Django 4.1.1 on 2022-12-02 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_banner_picturephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
