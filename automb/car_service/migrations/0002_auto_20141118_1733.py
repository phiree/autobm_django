# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service2',
            name='title',
            field=models.CharField(max_length=100, default=datetime.datetime(2014, 11, 18, 9, 33, 57, 998878, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service2',
            name='description',
            field=models.CharField(max_length=8000),
            preserve_default=True,
        ),
    ]
