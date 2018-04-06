# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20180406_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 11, 56, 27, 220245, tzinfo=utc), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 11, 56, 27, 220245, tzinfo=utc), verbose_name='date'),
        ),
    ]
