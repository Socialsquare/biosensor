# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-19 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20170219_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invitation',
            new_name='SchoolClassCode',
        ),
        migrations.AlterField(
            model_name='schoolclasscode',
            name='school_class',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.SchoolClass'),
        ),
    ]
