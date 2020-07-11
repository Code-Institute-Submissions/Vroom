# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-10 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('address1', models.CharField(max_length=80)),
                ('address2', models.CharField(blank=True, max_length=80)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_days', models.IntegerField()),
                ('addon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.Addon')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.Car')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
            ],
        ),
    ]
