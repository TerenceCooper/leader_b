# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161016_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.CharField(max_length=75),
        ),
    ]
