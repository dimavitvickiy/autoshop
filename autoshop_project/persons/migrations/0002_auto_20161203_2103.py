# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='level',
        ),
        migrations.DeleteModel(
            name='ManagerLevel',
        ),
    ]
