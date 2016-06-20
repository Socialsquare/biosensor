# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobricks', '0007_auto_20160606_0810'),
        ('studentgroups', '0009_auto_20160616_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroupbiosensor',
            name='biosensor',
        ),
        migrations.RemoveField(
            model_name='studentgroupbiosensor',
            name='student_group',
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='biosensors',
            field=models.ManyToManyField(to='biobricks.Biosensor'),
        ),
        migrations.DeleteModel(
            name='StudentGroupBiosensor',
        ),
    ]