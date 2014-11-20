# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0002_auto_20141118_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.CharField(max_length=10, choices=[('已预订', 'orderd'), ('已付款', 'paid'), ('已完成', 'complete')], default='orderd'),
            preserve_default=False,
        ),
    ]
