# Generated by Django 4.1.1 on 2023-04-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_conditiongeneral_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestatire',
            name='date_time',
        ),
        migrations.AddField(
            model_name='prestatire',
            name='profile',
            field=models.FileField(default=1, max_length=500, upload_to='img_profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestatire',
            name='resto',
            field=models.FileField(default=1, max_length=500, upload_to='img_id_card'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestatire',
            name='verso',
            field=models.FileField(default=1, max_length=500, upload_to='img_id_card'),
            preserve_default=False,
        ),
    ]
