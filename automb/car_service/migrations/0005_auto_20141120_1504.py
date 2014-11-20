# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0004_auto_20141120_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='complete_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 7, 4, 1, 671234, tzinfo=utc)),
            preserve_default=True,
        ),

    ]
