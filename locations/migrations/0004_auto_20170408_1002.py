# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20170318_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='coordinates_x',
            field=models.DecimalField(decimal_places=14, max_digits=16),
        ),
        migrations.AlterField(
            model_name='location',
            name='coordinates_y',
            field=models.DecimalField(decimal_places=14, max_digits=16),
        ),
    ]
