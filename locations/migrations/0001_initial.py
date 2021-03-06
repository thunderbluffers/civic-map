# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=10240)),
                ('coordinates_x', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coordinates_y', models.DecimalField(decimal_places=2, max_digits=5)),
                ('program', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=65535)),
                ('mark', models.PositiveSmallIntegerField(choices=[(1, 'Mark 1'), (2, 'Mark 2'), (3, 'Mark 3'), (4, 'Mark 4'), (5, 'Mark 5')], default=1)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
