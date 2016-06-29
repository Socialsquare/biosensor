# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-29 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import studentgroups.models


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0003_studentreport_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreport',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=studentgroups.models.do_upload_attachment),
        ),
    ]
