# Generated by Django 2.1.5 on 2019-02-14 10:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_uploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(height_field='img_height', storage=django.core.files.storage.FileSystemStorage(base_url='/img/', location='/Users/alanking/Desktop/app_media'), upload_to='%Y/%m/%d/', width_field='img_width'),
        ),
    ]