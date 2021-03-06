# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_historicallocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallocation',
            name='credibility',
        ),
        migrations.RemoveField(
            model_name='location',
            name='credibility',
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='_credibility',
            field=models.DecimalField(db_column='credibility', decimal_places=4, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='location',
            name='_credibility',
            field=models.DecimalField(db_column='credibility', decimal_places=4, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='tags',
            field=models.ManyToManyField(blank=True, to='locations.Tag'),
        ),
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Mark 1'), (2, 'Mark 2'), (3, 'Mark 3'), (4, 'Mark 4'), (5, 'Mark 5')], default=5),
        ),
    ]
