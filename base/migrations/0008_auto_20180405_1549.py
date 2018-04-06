# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20180405_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 5, 15, 49, 24, 290308, tzinfo=utc), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='allow_anonymous',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 5, 15, 49, 24, 290308, tzinfo=utc), verbose_name='date'),
        ),
    ]