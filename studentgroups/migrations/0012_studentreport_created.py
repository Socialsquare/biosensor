# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 14:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0011_auto_20160616_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreport',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 16, 14, 35, 50, 245270, tzinfo=utc)),
            preserve_default=False,
        ),
    ]