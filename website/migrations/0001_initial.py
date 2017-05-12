# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-15 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='full name')),
                ('company', models.CharField(max_length=120, verbose_name='company name')),
                ('email', models.EmailField(max_length=120, verbose_name='email address')),
                ('message', models.TextField()),
                ('email_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120, verbose_name='email address')),
            ],
        ),
    ]
