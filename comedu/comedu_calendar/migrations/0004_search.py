# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedu_calendar', '0003_auto_20170209_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=50, verbose_name='검색')),
            ],
        ),
    ]
