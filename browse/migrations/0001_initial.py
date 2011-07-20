# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Developer'
        db.create_table('browse_developer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('browse', ['Developer'])

        # Adding model 'Thumbnail'
        db.create_table('browse_thumbnail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('browse', ['Thumbnail'])

        # Adding model 'Device'
        db.create_table('browse_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('browse', ['Device'])

        # Adding model 'Category'
        db.create_table('browse_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('browse', ['Category'])

        # Adding model 'App'
        db.create_table('browse_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('rating', self.gf('django.db.models.fields.CharField')(default='0', max_length=4, null=True, blank=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['browse.Developer'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.CharField')(default='FREE', max_length=10, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category', to=orm['browse.Category'])),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('browse', ['App'])

        # Adding M2M table for field thumbnails on 'App'
        db.create_table('browse_app_thumbnails', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm['browse.app'], null=False)),
            ('thumbnail', models.ForeignKey(orm['browse.thumbnail'], null=False))
        ))
        db.create_unique('browse_app_thumbnails', ['app_id', 'thumbnail_id'])

        # Adding M2M table for field device on 'App'
        db.create_table('browse_app_device', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm['browse.app'], null=False)),
            ('device', models.ForeignKey(orm['browse.device'], null=False))
        ))
        db.create_unique('browse_app_device', ['app_id', 'device_id'])

        # Adding model 'morelinks'
        db.create_table('browse_morelinks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='morelinks', to=orm['browse.App'])),
        ))
        db.send_create_signal('browse', ['morelinks'])


    def backwards(self, orm):
        
        # Deleting model 'Developer'
        db.delete_table('browse_developer')

        # Deleting model 'Thumbnail'
        db.delete_table('browse_thumbnail')

        # Deleting model 'Device'
        db.delete_table('browse_device')

        # Deleting model 'Category'
        db.delete_table('browse_category')

        # Deleting model 'App'
        db.delete_table('browse_app')

        # Removing M2M table for field thumbnails on 'App'
        db.delete_table('browse_app_thumbnails')

        # Removing M2M table for field device on 'App'
        db.delete_table('browse_app_device')

        # Deleting model 'morelinks'
        db.delete_table('browse_morelinks')


    models = {
        'browse.app': {
            'Meta': {'object_name': 'App'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'to': "orm['browse.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['browse.Developer']", 'null': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'device'", 'symmetrical': 'False', 'to': "orm['browse.Device']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'price': ('django.db.models.fields.CharField', [], {'default': "'FREE'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'thumbnails': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['browse.Thumbnail']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'browse.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'browse.developer': {
            'Meta': {'object_name': 'Developer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'browse.device': {
            'Meta': {'object_name': 'Device'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'browse.morelinks': {
            'Meta': {'object_name': 'morelinks'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'morelinks'", 'to': "orm['browse.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'browse.thumbnail': {
            'Meta': {'object_name': 'Thumbnail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['browse']
