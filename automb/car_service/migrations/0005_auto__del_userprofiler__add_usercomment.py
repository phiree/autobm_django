# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfiler'
        db.delete_table('car_service_userprofiler')

        # Adding model 'UserComment'
        db.create_table('car_service_usercomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['car_service.Bill'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('stars_service', self.gf('django.db.models.fields.IntegerField')()),
            ('stars_treatment', self.gf('django.db.models.fields.IntegerField')()),
            ('stars_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('comment_content', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('comment_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 8, 0, 0))),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('car_service', ['UserComment'])


    def backwards(self, orm):
        # Adding model 'UserProfiler'
        db.create_table('car_service_userprofiler', (
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('car_service', ['UserProfiler'])

        # Deleting model 'UserComment'
        db.delete_table('car_service_usercomment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
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
            'created_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 8, 0, 0)'}),
            'final_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Service2']"}),
            'service_snapshot': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sms_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'ordered'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'car_service.carinfo': {
            'Meta': {'object_name': 'CarInfo'},
            'car_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.CarInfo']", 'null': 'True', 'blank': 'True'})
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
            'Meta': {'_ormbases': ['car_service.ServicePropertyValue'], 'object_name': 'ServicePropertyValue_Brand'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spv_brand'", 'to': "orm['car_service.ServicePropertyValue']"}),
            'servicepropertyvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue']"})
        },
        'car_service.servicepropertyvalue_brand_foiltype': {
            'Meta': {'_ormbases': ['car_service.ServicePropertyValue_Brand'], 'object_name': 'ServicePropertyValue_Brand_FoilType'},
            'foiltype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spv_b_foil'", 'to': "orm['car_service.ServicePropertyValue']"}),
            'servicepropertyvalue_brand_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['car_service.ServicePropertyValue_Brand']"})
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_close': ('django.db.models.fields.TimeField', [], {}),
            'time_open': ('django.db.models.fields.TimeField', [], {})
        },
        'car_service.usercomment': {
            'Meta': {'object_name': 'UserComment'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['car_service.Bill']"}),
            'comment_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'comment_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 8, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stars_cost': ('django.db.models.fields.IntegerField', [], {}),
            'stars_service': ('django.db.models.fields.IntegerField', [], {}),
            'stars_treatment': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['car_service']