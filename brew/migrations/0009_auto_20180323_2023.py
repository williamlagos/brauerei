# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-23 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0008_auto_20180307_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name=b'Foto'),
        ),
    ]
