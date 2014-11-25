# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bill.bill_code'
        db.add_column('car_service_bill', 'bill_code',
                      self.gf('django.db.models.fields.CharField')(max_length=20, default=123456),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bill.bill_code'
        db.delete_column('car_service_bill', 'bill_code')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'car_service.areainfo': {
            'Meta': {'object_name': 'AreaInfo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.AreaInfo']"})
        },
        'car_service.bill': {
            'Meta': {'object_name': 'Bill'},
            'bill_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complete_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'final_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'max_digits': '5'}),
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.CarInfo']"})
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
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'null': 'True', 'max_digits': '5'}),
            'price_market': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'null': 'True', 'max_digits': '5'}),
            'servicetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServiceType']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Supplier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'car_service.servicedetail': {
            'Meta': {'object_name': 'ServiceDetail'},
            'body_damage_size': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'body_damage_size'"}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'brand'"}),
            'car': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['car_service.Tree']", 'related_name': "'car'"}),
            'foil_model_front': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'foil_model_front'"}),
            'foil_model_sides_back': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'foil_model_sides_back'"}),
            'foil_type': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'foil_type'"}),
            'glass_damage_size': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'glass_damage_size'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_light_suit': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'main_light_suit'"}),
            'model_common': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'model_common'"}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'max_digits': '5'}),
            'price_preorder': ('django.db.models.fields.DecimalField', [], {'decimal_places': '0', 'max_digits': '5'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service']"}),
            'sound_proofing_type': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'sound_proofing_type'"}),
            'sound_suit': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'sound_suit'"}),
            'tire_repair_type': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']", 'related_name': "'tire_repair_type'"}),
            'wash_type': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']"})
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
            'servicepropertyvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue']"})
        },
        'car_service.servicepropertyvalue_brand_foiltype': {
            'Meta': {'_ormbases': ['car_service.ServicePropertyValue_Brand'], 'object_name': 'ServicePropertyValue_Brand_FoilType'},
            'foiltype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.ServicePropertyValue']", 'related_name': "'spv_b_foil'"}),
            'servicepropertyvalue_brand_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue_Brand']"})
        },
        'car_service.servicetype': {
            'Meta': {'object_name': 'ServiceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.ServiceType']"})
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Tree']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['car_service.Supplier']"}),
            'tree_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'car_service.userprofiler': {
            'Meta': {'object_name': 'UserProfiler'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['car_service']