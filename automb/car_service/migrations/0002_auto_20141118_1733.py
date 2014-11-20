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

        migrations.AlterField(
            model_name='service2',
            name='description',
            field=models.CharField(max_length=8000),
            preserve_default=True,
        ),
    ]
