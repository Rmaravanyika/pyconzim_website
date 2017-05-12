# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170422_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='website URL/ Twitter handler'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.CharField(choices=[('C', 'Corporate Sponsor'), ('I', 'Individual Sponsor')], max_length=1, verbose_name='sponsor type'),
        ),
    ]
