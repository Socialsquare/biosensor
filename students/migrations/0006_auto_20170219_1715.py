# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-19 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20170219_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.SchoolClass'),
        ),
    ]
