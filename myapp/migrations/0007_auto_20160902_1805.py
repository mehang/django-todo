# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 18:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160902_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completiondate',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 18, 5, 32, 422604)),
        ),
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.CharField(default='----', max_length=500),
        ),
    ]
