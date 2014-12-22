# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UniqueRandom'
        db.create_table('unique_random_uniquerandom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True)),
            ('test_data', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('unique_random', ['UniqueRandom'])


    def backwards(self, orm):
        # Deleting model 'UniqueRandom'
        db.delete_table('unique_random_uniquerandom')


    models = {
        'unique_random.uniquerandom': {
            'Meta': {'object_name': 'UniqueRandom'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_data': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['unique_random']