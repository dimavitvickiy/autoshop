# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('persons', '0003_delete_buyer'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_birthdate', models.DateField()),
                ('buyer_passport', models.CharField(max_length=20)),
                ('buyer_phone', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('deal_date', models.DateField()),
                ('deal_type', models.CharField(choices=[('TD', 'Test-Drive'), ('SL', 'Sale')], default='SL', max_length=2)),
                ('addition_equipment', models.ManyToManyField(to='equipments.AdditionEquipment')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.Manager')),
            ],
        ),
    ]
