# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biobricks', '0007_auto_20160606_0810'),
        ('studentgroups', '0007_studentreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBiosensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biosensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobricks.Biosensor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biosensors', to='studentgroups.StudentGroup')),
            ],
        ),
    ]