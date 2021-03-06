# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 13:18
from __future__ import unicode_literals

import car_models.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=car_models.models.upload_location, width_field='width_field'),
        ),
    ]
