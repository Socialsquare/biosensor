# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-08 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0002_studentgroup_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'ordering': ['name']},
        ),
    ]