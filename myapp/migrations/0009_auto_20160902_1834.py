# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 18:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160902_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completiondate',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 18, 34, 27, 247176)),
        ),
    ]
