# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160901_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completion_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]