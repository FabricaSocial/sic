# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Capacitando.inicio_atividades'
        db.alter_column('Capacitando', 'inicio_atividades', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Capacitando.familia'
        db.alter_column('Capacitando', 'familia', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Capacitando.atualizacao_cadastral'
        db.alter_column('Capacitando', 'atualizacao_cadastral', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Capacitando.inicio_atividades'
        db.alter_column('Capacitando', 'inicio_atividades', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Capacitando.familia'
        db.alter_column('Capacitando', 'familia', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Capacitando.atualizacao_cadastral'
        db.alter_column('Capacitando', 'atualizacao_cadastral', self.gf('django.db.models.fields.DateField')(default=None))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'modelos.areaatuacao': {
            'Meta': {'object_name': 'AreaAtuacao', 'db_table': "'AreaAtuacao'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.capacitando': {
            'Meta': {'object_name': 'Capacitando', 'db_table': "'Capacitando'"},
            'area_atuacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.AreaAtuacao']"}),
            'atualizacao_cadastral': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Categoria']"}),
            'data_registro': ('django.db.models.fields.DateField', [], {}),
            'especialidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Especialidade']"}),
            'familia': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'hora_registro': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacao_social': ('django.db.models.fields.BigIntegerField', [], {}),
            'inicio_atividades': ('django.db.models.fields.DateField', [], {}),
            'matricula': ('django.db.models.fields.BigIntegerField', [], {}),
            'necessidade_especial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.NecessidadeEspecial']"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'renda_per_capita': ('django.db.models.fields.FloatField', [], {}),
            'responsavel_familia': ('django.db.models.fields.BooleanField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'turno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Turno']"}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Unidade']"})
        },
        u'modelos.carteiratrabalho': {
            'Meta': {'object_name': 'CarteiraTrabalho', 'db_table': "'CarteiraTrabalho'"},
            'ctps': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'serie': ('django.db.models.fields.IntegerField', [], {})
        },
        u'modelos.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "'Categoria'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.categoriacnh': {
            'Meta': {'object_name': 'CategoriaCNH', 'db_table': "'CategoriaCNH'"},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.cidade': {
            'Meta': {'object_name': 'Cidade', 'db_table': "'Cidade'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']"})
        },
        u'modelos.cnh': {
            'Meta': {'object_name': 'CNH', 'db_table': "'CNH'"},
            'categoria_cnh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.CategoriaCNH']"}),
            'data_emissao': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.BigIntegerField', [], {}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']"}),
            'validade': ('django.db.models.fields.DateField', [], {})
        },
        u'modelos.desligamento': {
            'Meta': {'object_name': 'Desligamento', 'db_table': "'Desligamento'"},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']"}),
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.email': {
            'Meta': {'object_name': 'Email', 'db_table': "'Email'"},
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"})
        },
        u'modelos.endereco': {
            'Meta': {'object_name': 'Endereco', 'db_table': "'Endereco'"},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cep': ('django.db.models.fields.BigIntegerField', [], {}),
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']"}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.especialidade': {
            'Meta': {'object_name': 'Especialidade', 'db_table': "'Especialidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.estadocivil': {
            'Meta': {'object_name': 'EstadoCivil', 'db_table': "'EstadoCivil'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.etnia': {
            'Meta': {'object_name': 'Etnia', 'db_table': "'Etnia'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.filiacao': {
            'Meta': {'object_name': 'Filiacao', 'db_table': "'Filiacao'"},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"})
        },
        u'modelos.nacionalidade': {
            'Meta': {'object_name': 'Nacionalidade', 'db_table': "'Nacionalidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.naturalidade': {
            'Meta': {'object_name': 'Naturalidade', 'db_table': "'Naturalidade'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'})
        },
        u'modelos.necessidadeespecial': {
            'Meta': {'object_name': 'NecessidadeEspecial', 'db_table': "'NecessidadeEspecial'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.pais': {
            'Meta': {'object_name': 'Pais', 'db_table': "'Pais'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'modelos.pessoa': {
            'Meta': {'object_name': 'Pessoa', 'db_table': "'Pessoa'"},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.EstadoCivil']"}),
            'etnia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Etnia']"}),
            'filhos': ('django.db.models.fields.BooleanField', [], {}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Nacionalidade']"}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Naturalidade']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sexo': ('django.db.models.fields.BooleanField', [], {}),
            'tipo_identidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoIdentidade']"})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto', 'db_table': "'Ponto'"},
            'atraso': ('django.db.models.fields.TimeField', [], {}),
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']"}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_ponto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoPonto']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'modelos.registrogeral': {
            'Meta': {'object_name': 'RegistroGeral', 'db_table': "'RegistroGeral'"},
            'data_expedicao': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgao_expedidor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'rg': ('django.db.models.fields.BigIntegerField', [], {}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']"})
        },
        u'modelos.reservista': {
            'Meta': {'object_name': 'Reservista', 'db_table': "'Reservista'"},
            'certificado': ('django.db.models.fields.BigIntegerField', [], {}),
            'dispensa_incorporacao': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'serie': ('django.db.models.fields.BigIntegerField', [], {}),
            'unidade_alistamento': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'modelos.servicomilitar': {
            'Meta': {'object_name': 'ServicoMilitar', 'db_table': "'ServicoMilitar'"},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']"})
        },
        u'modelos.telefone': {
            'Meta': {'object_name': 'Telefone', 'db_table': "'Telefone'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.BigIntegerField', [], {}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'tipo_telefone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoTelefone']"})
        },
        u'modelos.tipoidentidade': {
            'Meta': {'object_name': 'TipoIdentidade', 'db_table': "'TipoIdentidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tipoponto': {
            'Meta': {'object_name': 'TipoPonto', 'db_table': "'TipoPonto'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tipotelefone': {
            'Meta': {'object_name': 'TipoTelefone', 'db_table': "'TipoTelefone'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tituloeleitor': {
            'Meta': {'object_name': 'TituloEleitor', 'db_table': "'TituloEleitor'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']"}),
            'secao': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.BigIntegerField', [], {}),
            'zona': ('django.db.models.fields.IntegerField', [], {})
        },
        u'modelos.turno': {
            'Meta': {'object_name': 'Turno', 'db_table': "'Turno'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'entrada': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'entrada_lanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saida': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'saida_lanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'modelos.uf': {
            'Meta': {'object_name': 'UF', 'db_table': "'UF'"},
            'abreviacao': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']"})
        },
        u'modelos.unidade': {
            'Meta': {'object_name': 'Unidade', 'db_table': "'Unidade'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['modelos']