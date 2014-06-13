# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ponto.capacitando'
        db.alter_column(u'modelos_ponto', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['access_db.Tabfuncionarios']))

    def backwards(self, orm):

        # Changing field 'Ponto.capacitando'
        db.alter_column(u'modelos_ponto', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['access_db.Tbassiduidade']))

    models = {
        u'access_db.tabfuncionarios': {
            'Meta': {'object_name': 'Tabfuncionarios', 'db_table': "u'TabFuncionarios'", 'managed': 'False'},
            'acl': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ACL'", 'blank': 'True'}),
            'anoservico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AnoServico'", 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'Bairro'", 'blank': 'True'}),
            'cartestrangeiro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'CartEstrangeiro'", 'blank': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'Categoria'", 'blank': 'True'}),
            'categoriacr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'CategoriaCR'", 'blank': 'True'}),
            'cdfamilia': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cdi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CDI'", 'blank': 'True'}),
            'cep': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'CEP'", 'blank': 'True'}),
            'cg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CG'", 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'Cidade'", 'blank': 'True'}),
            'cnh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'CNH'", 'blank': 'True'}),
            'codcpf': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'CodCPF'"}),
            'conjuge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11', 'db_column': "u'CPF'"}),
            'creserva': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Creserva'", 'blank': 'True'}),
            'ctps': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'CTPS'", 'blank': 'True'}),
            'datacnh': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datadesliga': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'Datadesliga'", 'blank': 'True'}),
            'dataexp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DataExp'", 'blank': 'True'}),
            'datanascimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DataNascimento'", 'blank': 'True'}),
            'datareg': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diativ': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DIAtiv'", 'blank': 'True'}),
            'dtinclusao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dtpis': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DtPis'", 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Email'", 'blank': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Endereco'", 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "u'Estado'", 'blank': 'True'}),
            'estadocivil': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'EstadoCivil'", 'blank': 'True'}),
            'filhos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Filhos'", 'blank': 'True'}),
            'horareg': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'limiteat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'localfoto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'LocalFoto'", 'blank': 'True'}),
            'matricula': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'municipiot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Municipiot'", 'blank': 'True'}),
            'nac': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Nac'", 'blank': 'True'}),
            'nat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Nat'", 'blank': 'True'}),
            'nis': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'NIS'", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Nome'", 'blank': 'True'}),
            'nomemae': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'NomeMae'", 'blank': 'True'}),
            'nomepai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'NomePai'", 'blank': 'True'}),
            'orgaocr': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'orgaoexpedidor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'OrgaoExpedidor'", 'blank': 'True'}),
            'paisorigem': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'PaisOrigem'", 'blank': 'True'}),
            'pcd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PCD'", 'blank': 'True'}),
            'pi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PI'", 'blank': 'True'}),
            'pispasep': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PISPasep'", 'blank': 'True'}),
            'pne': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PNE'", 'blank': 'True'}),
            'qualdef': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'QualDef'", 'blank': 'True'}),
            'ra_a': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "u'Ra\\xe7a'", 'blank': 'True'}),
            'rc': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'RC'", 'decimal_places': '4', 'max_digits': '19'}),
            'responsavel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'RG'", 'blank': 'True'}),
            's_riectps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'S\\xe9rieCTPS'", 'blank': 'True'}),
            'se_ot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Se\\xe7\\xe3ot'", 'blank': 'True'}),
            'seriecr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SerieCR'", 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'Sexo'", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Status'", 'blank': 'True'}),
            'subarea': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telefonecelular': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'TelefoneCelular'", 'blank': 'True'}),
            'telefoneres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'TelefoneRes'", 'blank': 'True'}),
            'tituloeleitor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'TituloEleitor'", 'blank': 'True'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "u'UF'", 'blank': 'True'}),
            'ufcnh': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "u'UFcnh'", 'blank': 'True'}),
            'ufexp': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "u'UFexp'", 'blank': 'True'}),
            'ufservico': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "u'UFservico'", 'blank': 'True'}),
            'uft': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'UFt'", 'blank': 'True'}),
            'umilitar': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_column': "u'UMilitar'", 'blank': 'True'}),
            'unidade': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'Unidade'", 'blank': 'True'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'validadecnh': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'zonat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Zonat'", 'blank': 'True'})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto'},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['access_db.Tabfuncionarios']"}),
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