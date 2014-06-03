# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'access_db.tbassiduidade': {
            'Meta': {'object_name': 'Tbassiduidade', 'db_table': "u'tbAssiduidade'", 'managed': 'False'},
            'cda': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'datai': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datar': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'horar': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'horar2': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'horar3': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'horar4': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'matricula': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto'},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['access_db.Tbassiduidade']"}),
            'dia': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_entrada': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoEntrada']"})
        },
        u'modelos.tipoentrada': {
            'Meta': {'object_name': 'TipoEntrada'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['modelos']
    symmetrical = True
