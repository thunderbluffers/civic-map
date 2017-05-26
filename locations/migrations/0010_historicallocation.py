# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0009_auto_20170526_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLocation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=10240)),
                ('latitude', models.DecimalField(decimal_places=18, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=18, max_digits=20)),
                ('program', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=255)),
                ('credibility', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical location',
            },
        ),
    ]
