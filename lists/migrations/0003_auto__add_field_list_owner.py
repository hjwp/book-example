# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'List.owner'
        db.add_column('lists_list', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['accounts.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'List.owner'
        db.delete_column('lists_list', 'owner_id')


    models = {
        'accounts.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'lists.item': {
            'Meta': {'object_name': 'Item', 'unique_together': "(('list', 'text'),)", 'ordering': "('id',)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lists.List']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'lists.list': {
            'Meta': {'object_name': 'List'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['accounts.User']"})
        }
    }

    complete_apps = ['lists']