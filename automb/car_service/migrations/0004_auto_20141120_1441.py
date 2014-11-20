# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0003_bill_status'),
    ]

    operations = [

        migrations.AlterField(
            model_name='servicepropertyvalue_brand_foiltype',
            name='foiltype',
            field=models.ForeignKey(to='car_service.ServicePropertyValue', verbose_name='贴膜类型', related_name='spv_b_foil'),
            preserve_default=True,
        ),
    ]
