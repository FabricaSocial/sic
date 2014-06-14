# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoriaCNH'
        db.create_table('CategoriaCNH', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['CategoriaCNH'])

        # Adding model 'Nacionalidade'
        db.create_table('Nacionalidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Nacionalidade'])

        # Adding model 'TipoIdentidade'
        db.create_table('TipoIdentidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['TipoIdentidade'])

        # Adding model 'TipoTelefone'
        db.create_table('TipoTelefone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['TipoTelefone'])

        # Adding model 'Pais'
        db.create_table('Pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Pais'])

        # Adding model 'Etnia'
        db.create_table('Etnia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Etnia'])

        # Adding model 'UF'
        db.create_table('UF', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pais'])),
            ('abreviacao', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['UF'])

        # Adding model 'Cidade'
        db.create_table('Cidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Cidade'])

        # Adding model 'Naturalidade'
        db.create_table('Naturalidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pais'])),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'])),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'])),
        ))
        db.send_create_signal(u'modelos', ['Naturalidade'])

        # Adding model 'Endereco'
        db.create_table('Endereco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cep', self.gf('django.db.models.fields.BigIntegerField')()),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'])),
        ))
        db.send_create_signal(u'modelos', ['Endereco'])

        # Adding model 'EstadoCivil'
        db.create_table('EstadoCivil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['EstadoCivil'])

        # Adding model 'Pessoa'
        db.create_table('Pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cpf', self.gf('django.db.models.fields.BigIntegerField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.BooleanField')()),
            ('filhos', self.gf('django.db.models.fields.BooleanField')()),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('etnia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Etnia'])),
            ('tipo_identidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoIdentidade'])),
            ('estado_civil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.EstadoCivil'])),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Endereco'])),
            ('nacionalidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Nacionalidade'])),
            ('naturalidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Naturalidade'])),
        ))
        db.send_create_signal(u'modelos', ['Pessoa'])

        # Adding model 'Reservista'
        db.create_table('Reservista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('certificado', self.gf('django.db.models.fields.BigIntegerField')()),
            ('serie', self.gf('django.db.models.fields.BigIntegerField')()),
            ('orgao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dispensa_incorporacao', self.gf('django.db.models.fields.BigIntegerField')()),
            ('unidade_alistamento', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['Reservista'])

        # Adding model 'RegistroGeral'
        db.create_table('RegistroGeral', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rg', self.gf('django.db.models.fields.BigIntegerField')()),
            ('orgao_expedidor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_expedicao', self.gf('django.db.models.fields.DateField')()),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'])),
        ))
        db.send_create_signal(u'modelos', ['RegistroGeral'])

        # Adding model 'ServicoMilitar'
        db.create_table('ServicoMilitar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'])),
        ))
        db.send_create_signal(u'modelos', ['ServicoMilitar'])

        # Adding model 'CarteiraTrabalho'
        db.create_table('CarteiraTrabalho', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ctps', self.gf('django.db.models.fields.BigIntegerField')()),
            ('serie', self.gf('django.db.models.fields.IntegerField')()),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['CarteiraTrabalho'])

        # Adding model 'Filiacao'
        db.create_table('Filiacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cpf', self.gf('django.db.models.fields.BigIntegerField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['Filiacao'])

        # Adding model 'CNH'
        db.create_table('CNH', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.BigIntegerField')()),
            ('data_emissao', self.gf('django.db.models.fields.DateField')()),
            ('validade', self.gf('django.db.models.fields.DateField')()),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'])),
            ('categoria_cnh', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.CategoriaCNH'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['CNH'])

        # Adding model 'Telefone'
        db.create_table('Telefone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.BigIntegerField')()),
            ('tipo_telefone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoTelefone'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['Telefone'])

        # Adding model 'Email'
        db.create_table('Email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
        ))
        db.send_create_signal(u'modelos', ['Email'])

        # Adding model 'TituloEleitor'
        db.create_table('TituloEleitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.BigIntegerField')()),
            ('zona', self.gf('django.db.models.fields.IntegerField')()),
            ('secao', self.gf('django.db.models.fields.IntegerField')()),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'])),
        ))
        db.send_create_signal(u'modelos', ['TituloEleitor'])

        # Adding model 'Categoria'
        db.create_table('Categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Categoria'])

        # Adding model 'NecessidadeEspecial'
        db.create_table('NecessidadeEpecial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['NecessidadeEspecial'])

        # Adding model 'Especialidade'
        db.create_table('Especialidades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['Especialidade'])

        # Adding model 'AreaAtuacao'
        db.create_table('AreaAtuacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['AreaAtuacao'])

        # Adding model 'Unidade'
        db.create_table('Unidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'])),
        ))
        db.send_create_signal(u'modelos', ['Unidade'])

        # Adding model 'Turno'
        db.create_table('Turno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('entrada', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('saida_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('entrada_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('saida', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'modelos', ['Turno'])

        # Adding model 'Capacitando'
        db.create_table('Capacitando', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('matricula', self.gf('django.db.models.fields.BigIntegerField')()),
            ('identificacao_social', self.gf('django.db.models.fields.BigIntegerField')()),
            ('responsavel_familia', self.gf('django.db.models.fields.BooleanField')()),
            ('familia', self.gf('django.db.models.fields.BigIntegerField')()),
            ('renda_per_capita', self.gf('django.db.models.fields.FloatField')()),
            ('atualizacao_cadastral', self.gf('django.db.models.fields.DateField')()),
            ('inicio_atividades', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
            ('data_registro', self.gf('django.db.models.fields.DateField')()),
            ('hora_registro', self.gf('django.db.models.fields.TimeField')()),
            ('area_atuacao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.AreaAtuacao'])),
            ('especialidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Especialidade'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'])),
            ('necessidade_especial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.NecessidadeEspecial'])),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Categoria'])),
            ('unidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Unidade'])),
            ('turno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Turno'])),
        ))
        db.send_create_signal(u'modelos', ['Capacitando'])

        # Adding model 'Desligamento'
        db.create_table('Desligamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('capacitando', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Capacitando'])),
        ))
        db.send_create_signal(u'modelos', ['Desligamento'])

        # Adding model 'TipoPonto'
        db.create_table('TipoPonto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'modelos', ['TipoPonto'])

        # Adding model 'Ponto'
        db.create_table('Ponto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('hora', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('tipo_ponto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoPonto'])),
            ('capacitando', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Capacitando'])),
        ))
        db.send_create_signal(u'modelos', ['Ponto'])


    def backwards(self, orm):
        # Deleting model 'CategoriaCNH'
        db.delete_table('CategoriaCNH')

        # Deleting model 'Nacionalidade'
        db.delete_table('Nacionalidade')

        # Deleting model 'TipoIdentidade'
        db.delete_table('TipoIdentidade')

        # Deleting model 'TipoTelefone'
        db.delete_table('TipoTelefone')

        # Deleting model 'Pais'
        db.delete_table('Pais')

        # Deleting model 'Etnia'
        db.delete_table('Etnia')

        # Deleting model 'UF'
        db.delete_table('UF')

        # Deleting model 'Cidade'
        db.delete_table('Cidade')

        # Deleting model 'Naturalidade'
        db.delete_table('Naturalidade')

        # Deleting model 'Endereco'
        db.delete_table('Endereco')

        # Deleting model 'EstadoCivil'
        db.delete_table('EstadoCivil')

        # Deleting model 'Pessoa'
        db.delete_table('Pessoa')

        # Deleting model 'Reservista'
        db.delete_table('Reservista')

        # Deleting model 'RegistroGeral'
        db.delete_table('RegistroGeral')

        # Deleting model 'ServicoMilitar'
        db.delete_table('ServicoMilitar')

        # Deleting model 'CarteiraTrabalho'
        db.delete_table('CarteiraTrabalho')

        # Deleting model 'Filiacao'
        db.delete_table('Filiacao')

        # Deleting model 'CNH'
        db.delete_table('CNH')

        # Deleting model 'Telefone'
        db.delete_table('Telefone')

        # Deleting model 'Email'
        db.delete_table('Email')

        # Deleting model 'TituloEleitor'
        db.delete_table('TituloEleitor')

        # Deleting model 'Categoria'
        db.delete_table('Categoria')

        # Deleting model 'NecessidadeEspecial'
        db.delete_table('NecessidadeEpecial')

        # Deleting model 'Especialidade'
        db.delete_table('Especialidades')

        # Deleting model 'AreaAtuacao'
        db.delete_table('AreaAtuacao')

        # Deleting model 'Unidade'
        db.delete_table('Unidade')

        # Deleting model 'Turno'
        db.delete_table('Turno')

        # Deleting model 'Capacitando'
        db.delete_table('Capacitando')

        # Deleting model 'Desligamento'
        db.delete_table('Desligamento')

        # Deleting model 'TipoPonto'
        db.delete_table('TipoPonto')

        # Deleting model 'Ponto'
        db.delete_table('Ponto')


    models = {
        u'modelos.areaatuacao': {
            'Meta': {'object_name': 'AreaAtuacao', 'db_table': "'AreaAtuacao'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.capacitando': {
            'Meta': {'object_name': 'Capacitando', 'db_table': "'Capacitando'"},
            'area_atuacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.AreaAtuacao']"}),
            'atualizacao_cadastral': ('django.db.models.fields.DateField', [], {}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Categoria']"}),
            'data_registro': ('django.db.models.fields.DateField', [], {}),
            'especialidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Especialidade']"}),
            'familia': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'Meta': {'object_name': 'Especialidade', 'db_table': "'Especialidades'"},
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
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']"}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']"})
        },
        u'modelos.necessidadeespecial': {
            'Meta': {'object_name': 'NecessidadeEspecial', 'db_table': "'NecessidadeEpecial'"},
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
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Nacionalidade']"}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Naturalidade']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sexo': ('django.db.models.fields.BooleanField', [], {}),
            'tipo_identidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoIdentidade']"})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto', 'db_table': "'Ponto'"},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']"}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_ponto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoPonto']"})
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