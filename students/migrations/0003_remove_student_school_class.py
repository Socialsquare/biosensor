# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-14 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_school_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school_class',
        ),
    ]
