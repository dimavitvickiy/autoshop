# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
