# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-26 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobricks', '0003_auto_20160627_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biosensor',
            name='problem_description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='biosensor',
            name='risk_description',
            field=models.TextField(max_length=10000),
        ),
    ]
