# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 22:24
from __future__ import unicode_literals

import autoshops.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoshops', '0004_auto_20161203_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoshop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=autoshops.models.upload_location),
        ),
    ]
