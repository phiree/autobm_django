# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AreaInfo'
        db.create_table('car_service_areainfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.AreaInfo'], null=True, blank=True)),
        ))
        db.send_create_signal('car_service', ['AreaInfo'])

        # Adding model 'ServiceType'
        db.create_table('car_service_servicetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServiceType'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('car_service', ['ServiceType'])

        # Adding model 'ServiceProperty'
        db.create_table('car_service_serviceproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('servicetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServiceType'])),
        ))
        db.send_create_signal('car_service', ['ServiceProperty'])

        # Adding model 'ServicePropertyValue'
        db.create_table('car_service_servicepropertyvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serviceproperty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServiceProperty'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_brand', self.gf('django.db.models.fields.BooleanField')()),
            ('is_foil_type', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('car_service', ['ServicePropertyValue'])

        # Adding model 'ServicePropertyValue_Brand'
        db.create_table('car_service_servicepropertyvalue_brand', (
            ('servicepropertyvalue_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['car_service.ServicePropertyValue'], primary_key=True, unique=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServicePropertyValue'], related_name='spv_brand')),
        ))
        db.send_create_signal('car_service', ['ServicePropertyValue_Brand'])

        # Adding model 'ServicePropertyValue_Brand_FoilType'
        db.create_table('car_service_servicepropertyvalue_brand_foiltype', (
            ('servicepropertyvalue_brand_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['car_service.ServicePropertyValue_Brand'], primary_key=True, unique=True)),
            ('foiltype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServicePropertyValue'], related_name='spv_b_foil')),
        ))
        db.send_create_signal('car_service', ['ServicePropertyValue_Brand_FoilType'])

        # Adding model 'CarInfo'
        db.create_table('car_service_carinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('car_type', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('info_type', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.CarInfo'], null=True, blank=True)),
        ))
        db.send_create_signal('car_service', ['CarInfo'])

        # Adding model 'Service2'
        db.create_table('car_service_service2', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Supplier'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=8000)),
            ('servicetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServiceType'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=0, max_digits=5, null=True)),
            ('price_market', self.gf('django.db.models.fields.DecimalField')(decimal_places=0, max_digits=5, null=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('car_service', ['Service2'])

        # Adding model 'ServiceValue'
        db.create_table('car_service_servicevalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Service2'])),
            ('servicepropertyvalue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.ServicePropertyValue'])),
        ))
        db.send_create_signal('car_service', ['ServiceValue'])

        # Adding model 'Tree'
        db.create_table('car_service_tree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tree_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('car_type', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, blank=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Supplier'], null=True, blank=True)),
        ))
        db.send_create_signal('car_service', ['Tree'])

        # Adding unique constraint on 'Tree', fields ['tree_type', 'name']
        db.create_unique('car_service_tree', ['tree_type', 'name'])

        # Adding model 'Supplier'
        db.create_table('car_service_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.AreaInfo'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('coordinate_x', self.gf('django.db.models.fields.FloatField')()),
            ('coordinate_y', self.gf('django.db.models.fields.FloatField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time_open', self.gf('django.db.models.fields.TimeField')()),
            ('time_close', self.gf('django.db.models.fields.TimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('car_service', ['Supplier'])

        # Adding model 'Service'
        db.create_table('car_service_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Supplier'])),
            ('service_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], related_name='service_type')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
        ))
        db.send_create_signal('car_service', ['Service'])

        # Adding model 'Car'
        db.create_table('car_service_car', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('car_service', ['Car'])

        # Adding model 'ServiceDetail'
        db.create_table('car_service_servicedetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Service'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='brand', blank=True)),
            ('wash_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, blank=True)),
            ('sound_proofing_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='sound_proofing_type', blank=True)),
            ('foil_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='foil_type', blank=True)),
            ('foil_model_front', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='foil_model_front', blank=True)),
            ('foil_model_sides_back', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='foil_model_sides_back', blank=True)),
            ('glass_damage_size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='glass_damage_size', blank=True)),
            ('tire_repair_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='tire_repair_type', blank=True)),
            ('body_damage_size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='body_damage_size', blank=True)),
            ('sound_suit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='sound_suit', blank=True)),
            ('main_light_suit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='main_light_suit', blank=True)),
            ('model_common', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Tree'], null=True, related_name='model_common', blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=0)),
            ('price_preorder', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=0)),
        ))
        db.send_create_signal('car_service', ['ServiceDetail'])

        # Adding M2M table for field car on 'ServiceDetail'
        m2m_table_name = db.shorten_name('car_service_servicedetail_car')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('servicedetail', models.ForeignKey(orm['car_service.servicedetail'], null=False)),
            ('tree', models.ForeignKey(orm['car_service.tree'], null=False))
        ))
        db.create_unique(m2m_table_name, ['servicedetail_id', 'tree_id'])

        # Adding model 'Bill'
        db.create_table('car_service_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Service2'])),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('service_snapshot', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('sms_content', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('final_price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0))),
            ('complete_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('car_service', ['Bill'])

        # Adding model 'promote_register'
        db.create_table('car_service_promote_register', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('car_service', ['promote_register'])

        # Adding model 'UserProfiler'
        db.create_table('car_service_userprofiler', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('car_service', ['UserProfiler'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tree', fields ['tree_type', 'name']
        db.delete_unique('car_service_tree', ['tree_type', 'name'])

        # Deleting model 'AreaInfo'
        db.delete_table('car_service_areainfo')

        # Deleting model 'ServiceType'
        db.delete_table('car_service_servicetype')

        # Deleting model 'ServiceProperty'
        db.delete_table('car_service_serviceproperty')

        # Deleting model 'ServicePropertyValue'
        db.delete_table('car_service_servicepropertyvalue')

        # Deleting model 'ServicePropertyValue_Brand'
        db.delete_table('car_service_servicepropertyvalue_brand')

        # Deleting model 'ServicePropertyValue_Brand_FoilType'
        db.delete_table('car_service_servicepropertyvalue_brand_foiltype')

        # Deleting model 'CarInfo'
        db.delete_table('car_service_carinfo')

        # Deleting model 'Service2'
        db.delete_table('car_service_service2')

        # Deleting model 'ServiceValue'
        db.delete_table('car_service_servicevalue')

        # Deleting model 'Tree'
        db.delete_table('car_service_tree')

        # Deleting model 'Supplier'
        db.delete_table('car_service_supplier')

        # Deleting model 'Service'
        db.delete_table('car_service_service')

        # Deleting model 'Car'
        db.delete_table('car_service_car')

        # Deleting model 'ServiceDetail'
        db.delete_table('car_service_servicedetail')

        # Removing M2M table for field car on 'ServiceDetail'
        db.delete_table(db.shorten_name('car_service_servicedetail_car'))

        # Deleting model 'Bill'
        db.delete_table('car_service_bill')

        # Deleting model 'promote_register'
        db.delete_table('car_service_promote_register')

        # Deleting model 'UserProfiler'
        db.delete_table('car_service_userprofiler')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'car_service.areainfo': {
            'Meta': {'object_name': 'AreaInfo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.AreaInfo']", 'null': 'True', 'blank': 'True'})
        },
        'car_service.bill': {
            'Meta': {'object_name': 'Bill'},
            'bill_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complete_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'final_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service2']"}),
            'service_snapshot': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sms_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'car_service.car': {
            'Meta': {'object_name': 'Car'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'car_service.carinfo': {
            'Meta': {'object_name': 'CarInfo'},
            'car_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.CarInfo']", 'null': 'True', 'blank': 'True'})
        },
        'car_service.promote_register': {
            'Meta': {'object_name': 'promote_register'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'car_service.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'related_name': "'service_type'"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Supplier']"})
        },
        'car_service.service2': {
            'Meta': {'object_name': 'Service2'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'max_digits': '5', 'null': 'True'}),
            'price_market': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'max_digits': '5', 'null': 'True'}),
            'servicetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceType']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Supplier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'car_service.servicedetail': {
            'Meta': {'object_name': 'ServiceDetail'},
            'body_damage_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'body_damage_size'", 'blank': 'True'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'brand'", 'blank': 'True'}),
            'car': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['car_service.Tree']", 'related_name': "'car'"}),
            'foil_model_front': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'foil_model_front'", 'blank': 'True'}),
            'foil_model_sides_back': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'foil_model_sides_back'", 'blank': 'True'}),
            'foil_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'foil_type'", 'blank': 'True'}),
            'glass_damage_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'glass_damage_size'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_light_suit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'main_light_suit'", 'blank': 'True'}),
            'model_common': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'model_common'", 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '0'}),
            'price_preorder': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '0'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service']"}),
            'sound_proofing_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'sound_proofing_type'", 'blank': 'True'}),
            'sound_suit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'sound_suit'", 'blank': 'True'}),
            'tire_repair_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'related_name': "'tire_repair_type'", 'blank': 'True'}),
            'wash_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'blank': 'True'})
        },
        'car_service.serviceproperty': {
            'Meta': {'object_name': 'ServiceProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'servicetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceType']"})
        },
        'car_service.servicepropertyvalue': {
            'Meta': {'object_name': 'ServicePropertyValue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_brand': ('django.db.models.fields.BooleanField', [], {}),
            'is_foil_type': ('django.db.models.fields.BooleanField', [], {}),
            'serviceproperty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceProperty']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'car_service.servicepropertyvalue_brand': {
            'Meta': {'_ormbases': ['car_service.ServicePropertyValue'], 'object_name': 'ServicePropertyValue_Brand'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServicePropertyValue']", 'related_name': "'spv_brand'"}),
            'servicepropertyvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['car_service.ServicePropertyValue']", 'primary_key': 'True', 'unique': 'True'})
        },
        'car_service.servicepropertyvalue_brand_foiltype': {
            'Meta': {'_ormbases': ['car_service.ServicePropertyValue_Brand'], 'object_name': 'ServicePropertyValue_Brand_FoilType'},
            'foiltype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServicePropertyValue']", 'related_name': "'spv_b_foil'"}),
            'servicepropertyvalue_brand_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['car_service.ServicePropertyValue_Brand']", 'primary_key': 'True', 'unique': 'True'})
        },
        'car_service.servicetype': {
            'Meta': {'object_name': 'ServiceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceType']", 'null': 'True', 'blank': 'True'})
        },
        'car_service.servicevalue': {
            'Meta': {'object_name': 'ServiceValue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service2']"}),
            'servicepropertyvalue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServicePropertyValue']"})
        },
        'car_service.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.AreaInfo']"}),
            'coordinate_x': ('django.db.models.fields.FloatField', [], {}),
            'coordinate_y': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'time_close': ('django.db.models.fields.TimeField', [], {}),
            'time_open': ('django.db.models.fields.TimeField', [], {})
        },
        'car_service.tree': {
            'Meta': {'unique_together': "(('tree_type', 'name'),)", 'object_name': 'Tree'},
            'car_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Tree']", 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Supplier']", 'null': 'True', 'blank': 'True'}),
            'tree_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'car_service.userprofiler': {
            'Meta': {'object_name': 'UserProfiler'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['car_service']