# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20170408_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='coordinates_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='coordinates_y',
            new_name='longitude',
        ),
    ]
