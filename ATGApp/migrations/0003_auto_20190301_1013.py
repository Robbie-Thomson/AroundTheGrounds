# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-01 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATGApp', '0002_auto_20190301_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='photo',
            field=models.ImageField(upload_to='stadium_images'),
        ),
    ]