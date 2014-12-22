# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Tree', fields ['tree_type', 'name']
        db.delete_unique('car_service_tree', ['tree_type', 'name'])

        # Deleting model 'Tree'
        db.delete_table('car_service_tree')

        # Deleting model 'Service'
        db.delete_table('car_service_service')

        # Deleting model 'ServiceDetail'
        db.delete_table('car_service_servicedetail')

        # Removing M2M table for field car on 'ServiceDetail'
        db.delete_table(db.shorten_name('car_service_servicedetail_car'))

        # Deleting model 'Car'
        db.delete_table('car_service_car')


    def backwards(self, orm):
        # Adding model 'Tree'
        db.create_table('car_service_tree', (
            ('car_type', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['car_service.Tree'])),
            ('tree_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['car_service.Supplier'])),
        ))
        db.send_create_signal('car_service', ['Tree'])

        # Adding unique constraint on 'Tree', fields ['tree_type', 'name']
        db.create_unique('car_service_tree', ['tree_type', 'name'])

        # Adding model 'Service'
        db.create_table('car_service_service', (
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Supplier'])),
            ('service_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='service_type', to=orm['car_service.Tree'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
        ))
        db.send_create_signal('car_service', ['Service'])

        # Adding model 'ServiceDetail'
        db.create_table('car_service_servicedetail', (
            ('tire_repair_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tire_repair_type', blank=True, null=True, to=orm['car_service.Tree'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sound_suit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sound_suit', blank=True, null=True, to=orm['car_service.Tree'])),
            ('foil_model_front', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foil_model_front', blank=True, null=True, to=orm['car_service.Tree'])),
            ('model_common', self.gf('django.db.models.fields.related.ForeignKey')(related_name='model_common', blank=True, null=True, to=orm['car_service.Tree'])),
            ('wash_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['car_service.Tree'])),
            ('body_damage_size', self.gf('django.db.models.fields.related.ForeignKey')(related_name='body_damage_size', blank=True, null=True, to=orm['car_service.Tree'])),
            ('foil_model_sides_back', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foil_model_sides_back', blank=True, null=True, to=orm['car_service.Tree'])),
            ('price_preorder', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=0)),
            ('glass_damage_size', self.gf('django.db.models.fields.related.ForeignKey')(related_name='glass_damage_size', blank=True, null=True, to=orm['car_service.Tree'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Service'])),
            ('main_light_suit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_light_suit', blank=True, null=True, to=orm['car_service.Tree'])),
            ('foil_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foil_type', blank=True, null=True, to=orm['car_service.Tree'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(related_name='brand', blank=True, null=True, to=orm['car_service.Tree'])),
            ('sound_proofing_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sound_proofing_type', blank=True, null=True, to=orm['car_service.Tree'])),
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

        # Adding model 'Car'
        db.create_table('car_service_car', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('car_service', ['Car'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'car_service.areainfo': {
            'Meta': {'object_name': 'AreaInfo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['car_service.AreaInfo']"})
        },
        'car_service.bill': {
            'Meta': {'object_name': 'Bill'},
            'bill_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complete_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
            'final_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service2']"}),
            'service_snapshot': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sms_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'ordered'", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'car_service.carinfo': {
            'Meta': {'object_name': 'CarInfo'},
            'car_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['car_service.CarInfo']"})
        },
        'car_service.promote_register': {
            'Meta': {'object_name': 'promote_register'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'car_service.service2': {
            'Meta': {'object_name': 'Service2'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'null': 'True', 'decimal_places': '0'}),
            'price_market': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'null': 'True', 'decimal_places': '0'}),
            'servicetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceType']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Supplier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'Meta': {'object_name': 'ServicePropertyValue_Brand', '_ormbases': ['car_service.ServicePropertyValue']},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spv_brand'", 'to': "orm['car_service.ServicePropertyValue']"}),
            'servicepropertyvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue']"})
        },
        'car_service.servicepropertyvalue_brand_foiltype': {
            'Meta': {'object_name': 'ServicePropertyValue_Brand_FoilType', '_ormbases': ['car_service.ServicePropertyValue_Brand']},
            'foiltype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spv_b_foil'", 'to': "orm['car_service.ServicePropertyValue']"}),
            'servicepropertyvalue_brand_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue_Brand']"})
        },
        'car_service.servicetype': {
            'Meta': {'object_name': 'ServiceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['car_service.ServiceType']"})
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_close': ('django.db.models.fields.TimeField', [], {}),
            'time_open': ('django.db.models.fields.TimeField', [], {})
        },
        'car_service.userprofiler': {
            'Meta': {'object_name': 'UserProfiler'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['car_service']