# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-06 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0010_auto_20170303_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreport',
            name='resume',
            field=models.CharField(max_length=10000),
        ),
    ]
