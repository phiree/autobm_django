# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(null=True, blank=True, to='car_service.AreaInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order_date', models.DateTimeField()),
                ('service_snapshot', models.CharField(max_length=2000)),
                ('sms_content', models.CharField(max_length=1000)),
                ('final_price', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('car_type', models.CharField(null=True, choices=[('small', '小型'), ('midium', '中型'), ('large', '大型')], blank=True, max_length=10)),
                ('info_type', models.CharField(null=True, choices=[('brand', '品牌'), ('series', '车系'), ('type', '型号')], blank=True, max_length=10)),
                ('parent', models.ForeignKey(null=True, blank=True, to='car_service.CarInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='promote_register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=4000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(null=True, decimal_places=0, max_digits=5)),
                ('price_market', models.DecimalField(null=True, decimal_places=0, max_digits=5)),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('price_preorder', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicePropertyValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=200)),
                ('is_brand', models.BooleanField()),
                ('is_foil_type', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicePropertyValue_Brand',
            fields=[
                ('servicepropertyvalue_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='car_service.ServicePropertyValue', auto_created=True)),
            ],
            options={
            },
            bases=('car_service.servicepropertyvalue',),
        ),
        migrations.CreateModel(
            name='ServicePropertyValue_Brand_FoilType',
            fields=[
                ('servicepropertyvalue_brand_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='car_service.ServicePropertyValue_Brand', auto_created=True)),
                ('foiltype', models.ForeignKey(related_name='spv_b_foil', to='car_service.ServicePropertyValue')),
            ],
            options={
            },
            bases=('car_service.servicepropertyvalue_brand',),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('parent', models.ForeignKey(null=True, blank=True, to='car_service.ServiceType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('service', models.ForeignKey(to='car_service.Service2')),
                ('servicepropertyvalue', models.ForeignKey(to='car_service.ServicePropertyValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=100)),
                ('address', models.CharField(verbose_name='地址', max_length=100)),
                ('coordinate_x', models.FloatField(verbose_name='经度')),
                ('coordinate_y', models.FloatField(verbose_name='维度')),
                ('photo', models.ImageField(null=True, upload_to='photos/suppliers', blank=True)),
                ('phone', models.CharField(max_length=100)),
                ('time_open', models.TimeField()),
                ('time_close', models.TimeField()),
                ('description', models.CharField(max_length=1000)),
                ('area', models.ForeignKey(to='car_service.AreaInfo', verbose_name='区域')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tree_type', models.CharField(choices=[('area', '区域'), ('car', '车型'), ('service', '服务'), ('brand', '品牌'), ('wash_type', '洗车方式'), ('sound_proofing_type', '隔音方式'), ('foil_type', '贴膜类型'), ('foil_model_front', '前挡型号'), ('foil_model_sides_back', '侧后挡型号'), ('glass_damage_size', '玻璃损坏尺寸'), ('tire_repair_type', '补胎类型'), ('body_damage_size', '车身损伤尺寸'), ('sound_suit', '音响套装'), ('main_light_suit', '大灯套装'), ('model_common', '型号')], max_length=100)),
                ('car_type', models.CharField(null=True, choices=[('small', '小型'), ('midium', '中型'), ('large', '大型')], blank=True, max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(null=True, blank=True, to='car_service.Tree')),
                ('supplier', models.ForeignKey(null=True, blank=True, to='car_service.Supplier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('phone', models.CharField(verbose_name='电话号码', max_length=140)),
                ('gender', models.CharField(verbose_name='性别', max_length=140)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tree',
            unique_together=set([('tree_type', 'name')]),
        ),
        migrations.AddField(
            model_name='servicepropertyvalue_brand',
            name='brand',
            field=models.ForeignKey(related_name='spv_brand', to='car_service.ServicePropertyValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicepropertyvalue',
            name='serviceproperty',
            field=models.ForeignKey(to='car_service.ServiceProperty', verbose_name='服务属性'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serviceproperty',
            name='servicetype',
            field=models.ForeignKey(to='car_service.ServiceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='body_damage_size',
            field=models.ForeignKey(null=True, blank=True, related_name='body_damage_size', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='brand',
            field=models.ForeignKey(null=True, blank=True, related_name='brand', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='car',
            field=models.ManyToManyField(related_name='car', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='foil_model_front',
            field=models.ForeignKey(null=True, blank=True, related_name='foil_model_front', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='foil_model_sides_back',
            field=models.ForeignKey(null=True, blank=True, related_name='foil_model_sides_back', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='foil_type',
            field=models.ForeignKey(null=True, blank=True, related_name='foil_type', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='glass_damage_size',
            field=models.ForeignKey(null=True, blank=True, related_name='glass_damage_size', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='main_light_suit',
            field=models.ForeignKey(null=True, blank=True, related_name='main_light_suit', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='model_common',
            field=models.ForeignKey(null=True, blank=True, related_name='model_common', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='service',
            field=models.ForeignKey(to='car_service.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='sound_proofing_type',
            field=models.ForeignKey(null=True, blank=True, related_name='sound_proofing_type', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='sound_suit',
            field=models.ForeignKey(null=True, blank=True, related_name='sound_suit', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='tire_repair_type',
            field=models.ForeignKey(null=True, blank=True, related_name='tire_repair_type', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='wash_type',
            field=models.ForeignKey(null=True, blank=True, to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service2',
            name='servicetype',
            field=models.ForeignKey(to='car_service.ServiceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service2',
            name='supplier',
            field=models.ForeignKey(to='car_service.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(related_name='service_type', to='car_service.Tree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='supplier',
            field=models.ForeignKey(to='car_service.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='service',
            field=models.ForeignKey(to='car_service.Service2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
