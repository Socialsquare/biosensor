# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-19 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_auto_20170219_2300'),
        ('studentgroups', '0006_auto_20170219_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='school',
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='school_class',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teachers.SchoolClass'),
            preserve_default=False,
        ),
    ]
