# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-08 21:09
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0004_studentreport_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='subject',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='Biologi', max_length=100, no_check_for_status=True),
        ),
    ]
