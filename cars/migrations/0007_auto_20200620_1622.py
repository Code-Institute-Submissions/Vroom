# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-20 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user_id',
            field=models.CharField(max_length=20),
        ),
    ]