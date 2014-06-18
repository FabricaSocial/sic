# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CarteiraTrabalho.serie'
        db.alter_column('CarteiraTrabalho', 'serie', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'CarteiraTrabalho.ctps'
        db.alter_column('CarteiraTrabalho', 'ctps', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'CarteiraTrabalho.pessoa'
        db.alter_column('CarteiraTrabalho', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'Nacionalidade.descricao'
        db.alter_column('Nacionalidade', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TipoTelefone.descricao'
        db.alter_column('TipoTelefone', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'EstadoCivil.descricao'
        db.alter_column('EstadoCivil', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Capacitando.categoria'
        db.alter_column('Capacitando', 'categoria_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Categoria'], null=True))

        # Changing field 'Capacitando.necessidade_especial'
        db.alter_column('Capacitando', 'necessidade_especial_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.NecessidadeEspecial'], null=True))

        # Changing field 'Capacitando.hora_registro'
        db.alter_column('Capacitando', 'hora_registro', self.gf('django.db.models.fields.TimeField')(null=True))

        # Changing field 'Capacitando.inicio_atividades'
        db.alter_column('Capacitando', 'inicio_atividades', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Capacitando.unidade'
        db.alter_column('Capacitando', 'unidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Unidade'], null=True))

        # Changing field 'Capacitando.area_atuacao'
        db.alter_column('Capacitando', 'area_atuacao_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.AreaAtuacao'], null=True))

        # Changing field 'Capacitando.especialidade'
        db.alter_column('Capacitando', 'especialidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Especialidade'], null=True))

        # Changing field 'Capacitando.data_registro'
        db.alter_column('Capacitando', 'data_registro', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Capacitando.turno'
        db.alter_column('Capacitando', 'turno_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Turno'], null=True))

        # Changing field 'Capacitando.pessoa'
        db.alter_column('Capacitando', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'Capacitando.renda_per_capita'
        db.alter_column('Capacitando', 'renda_per_capita', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Capacitando.matricula'
        db.alter_column('Capacitando', 'matricula', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Naturalidade.pais'
        db.alter_column('Naturalidade', 'pais_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pais'], null=True))

        # Changing field 'Pessoa.naturalidade'
        db.alter_column('Pessoa', 'naturalidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Naturalidade'], null=True))

        # Changing field 'Pessoa.nome'
        db.alter_column('Pessoa', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Pessoa.data_nascimento'
        db.alter_column('Pessoa', 'data_nascimento', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Pessoa.cpf'
        db.alter_column('Pessoa', 'cpf', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Pessoa.nacionalidade'
        db.alter_column('Pessoa', 'nacionalidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Nacionalidade'], null=True))

        # Changing field 'Pessoa.tipo_identidade'
        db.alter_column('Pessoa', 'tipo_identidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoIdentidade'], null=True))

        # Changing field 'Pessoa.etnia'
        db.alter_column('Pessoa', 'etnia_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Etnia'], null=True))

        # Changing field 'Pessoa.endereco'
        db.alter_column('Pessoa', 'endereco_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Endereco'], null=True))

        # Changing field 'Pessoa.estado_civil'
        db.alter_column('Pessoa', 'estado_civil_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.EstadoCivil'], null=True))

        # Changing field 'Unidade.cidade'
        db.alter_column('Unidade', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'], null=True))

        # Changing field 'TituloEleitor.zona'
        db.alter_column('TituloEleitor', 'zona', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'TituloEleitor.secao'
        db.alter_column('TituloEleitor', 'secao', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'TituloEleitor.cidade'
        db.alter_column('TituloEleitor', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'], null=True))

        # Changing field 'TituloEleitor.titulo'
        db.alter_column('TituloEleitor', 'titulo', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'TituloEleitor.pessoa'
        db.alter_column('TituloEleitor', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'NecessidadeEspecial.descricao'
        db.alter_column('NecessidadeEspecial', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Cidade.uf'
        db.alter_column('Cidade', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'], null=True))

        # Changing field 'Cidade.nome'
        db.alter_column('Cidade', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'AreaAtuacao.descricao'
        db.alter_column('AreaAtuacao', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Categoria.descricao'
        db.alter_column('Categoria', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'UF.pais'
        db.alter_column('UF', 'pais_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pais'], null=True))

        # Changing field 'UF.abreviacao'
        db.alter_column('UF', 'abreviacao', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'UF.nome'
        db.alter_column('UF', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Ponto.hora'
        db.alter_column('Ponto', 'hora', self.gf('django.db.models.fields.TimeField')(auto_now=True, null=True))

        # Changing field 'Ponto.capacitando'
        db.alter_column('Ponto', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Capacitando'], null=True))

        # Changing field 'Ponto.user'
        db.alter_column('Ponto', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Ponto.data'
        db.alter_column('Ponto', 'data', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True))

        # Changing field 'Ponto.tipo_ponto'
        db.alter_column('Ponto', 'tipo_ponto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoPonto'], null=True))

        # Changing field 'Etnia.descricao'
        db.alter_column('Etnia', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Filiacao.pessoa'
        db.alter_column('Filiacao', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'Filiacao.cpf'
        db.alter_column('Filiacao', 'cpf', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Filiacao.nome'
        db.alter_column('Filiacao', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Desligamento.capacitando'
        db.alter_column('Desligamento', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Capacitando'], null=True))

        # Changing field 'RegistroGeral.pessoa'
        db.alter_column('RegistroGeral', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'ServicoMilitar.pessoa'
        db.alter_column('ServicoMilitar', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'ServicoMilitar.ano'
        db.alter_column('ServicoMilitar', 'ano', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ServicoMilitar.uf'
        db.alter_column('ServicoMilitar', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'], null=True))

        # Changing field 'Endereco.endereco'
        db.alter_column('Endereco', 'endereco', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Endereco.cidade'
        db.alter_column('Endereco', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Cidade'], null=True))

        # Changing field 'Endereco.cep'
        db.alter_column('Endereco', 'cep', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Endereco.bairro'
        db.alter_column('Endereco', 'bairro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TipoIdentidade.descricao'
        db.alter_column('TipoIdentidade', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Email.endereco'
        db.alter_column('Email', 'endereco', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Email.pessoa'
        db.alter_column('Email', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'CategoriaCNH.categoria'
        db.alter_column('CategoriaCNH', 'categoria', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Pais.nome'
        db.alter_column('Pais', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Reservista.serie'
        db.alter_column('Reservista', 'serie', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Reservista.orgao'
        db.alter_column('Reservista', 'orgao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Reservista.dispensa_incorporacao'
        db.alter_column('Reservista', 'dispensa_incorporacao', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'Reservista.unidade_alistamento'
        db.alter_column('Reservista', 'unidade_alistamento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Reservista.pessoa'
        db.alter_column('Reservista', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'Reservista.certificado'
        db.alter_column('Reservista', 'certificado', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'CNH.validade'
        db.alter_column('CNH', 'validade', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'CNH.categoria_cnh'
        db.alter_column('CNH', 'categoria_cnh_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.CategoriaCNH'], null=True))

        # Changing field 'CNH.numero'
        db.alter_column('CNH', 'numero', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'CNH.data_emissao'
        db.alter_column('CNH', 'data_emissao', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'CNH.pessoa'
        db.alter_column('CNH', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'CNH.uf'
        db.alter_column('CNH', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.UF'], null=True))

        # Changing field 'TipoPonto.descricao'
        db.alter_column('TipoPonto', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Especialidade.descricao'
        db.alter_column('Especialidade', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Turno.saida_lanche'
        db.alter_column('Turno', 'saida_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, null=True))

        # Changing field 'Turno.saida'
        db.alter_column('Turno', 'saida', self.gf('django.db.models.fields.TimeField')(auto_now=True, null=True))

        # Changing field 'Turno.descricao'
        db.alter_column('Turno', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Turno.entrada_lanche'
        db.alter_column('Turno', 'entrada_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, null=True))

        # Changing field 'Turno.entrada'
        db.alter_column('Turno', 'entrada', self.gf('django.db.models.fields.TimeField')(auto_now=True, null=True))

        # Changing field 'Telefone.pessoa'
        db.alter_column('Telefone', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.Pessoa'], null=True))

        # Changing field 'Telefone.tipo_telefone'
        db.alter_column('Telefone', 'tipo_telefone_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modelos.TipoTelefone'], null=True))

        # Changing field 'Telefone.numero'
        db.alter_column('Telefone', 'numero', self.gf('django.db.models.fields.BigIntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'CarteiraTrabalho.serie'
        db.alter_column('CarteiraTrabalho', 'serie', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'CarteiraTrabalho.ctps'
        db.alter_column('CarteiraTrabalho', 'ctps', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'CarteiraTrabalho.pessoa'
        db.alter_column('CarteiraTrabalho', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'Nacionalidade.descricao'
        db.alter_column('Nacionalidade', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'TipoTelefone.descricao'
        db.alter_column('TipoTelefone', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'EstadoCivil.descricao'
        db.alter_column('EstadoCivil', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Capacitando.categoria'
        db.alter_column('Capacitando', 'categoria_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Categoria']))

        # Changing field 'Capacitando.necessidade_especial'
        db.alter_column('Capacitando', 'necessidade_especial_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.NecessidadeEspecial']))

        # Changing field 'Capacitando.hora_registro'
        db.alter_column('Capacitando', 'hora_registro', self.gf('django.db.models.fields.TimeField')(default=None))

        # Changing field 'Capacitando.inicio_atividades'
        db.alter_column('Capacitando', 'inicio_atividades', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Capacitando.unidade'
        db.alter_column('Capacitando', 'unidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Unidade']))

        # Changing field 'Capacitando.area_atuacao'
        db.alter_column('Capacitando', 'area_atuacao_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.AreaAtuacao']))

        # Changing field 'Capacitando.especialidade'
        db.alter_column('Capacitando', 'especialidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Especialidade']))

        # Changing field 'Capacitando.data_registro'
        db.alter_column('Capacitando', 'data_registro', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Capacitando.turno'
        db.alter_column('Capacitando', 'turno_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Turno']))

        # Changing field 'Capacitando.pessoa'
        db.alter_column('Capacitando', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'Capacitando.renda_per_capita'
        db.alter_column('Capacitando', 'renda_per_capita', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Capacitando.matricula'
        db.alter_column('Capacitando', 'matricula', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Naturalidade.pais'
        db.alter_column('Naturalidade', 'pais_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pais']))

        # Changing field 'Pessoa.naturalidade'
        db.alter_column('Pessoa', 'naturalidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Naturalidade']))

        # Changing field 'Pessoa.nome'
        db.alter_column('Pessoa', 'nome', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Pessoa.data_nascimento'
        db.alter_column('Pessoa', 'data_nascimento', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Pessoa.cpf'
        db.alter_column('Pessoa', 'cpf', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Pessoa.nacionalidade'
        db.alter_column('Pessoa', 'nacionalidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Nacionalidade']))

        # Changing field 'Pessoa.tipo_identidade'
        db.alter_column('Pessoa', 'tipo_identidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.TipoIdentidade']))

        # Changing field 'Pessoa.etnia'
        db.alter_column('Pessoa', 'etnia_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Etnia']))

        # Changing field 'Pessoa.endereco'
        db.alter_column('Pessoa', 'endereco_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Endereco']))

        # Changing field 'Pessoa.estado_civil'
        db.alter_column('Pessoa', 'estado_civil_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.EstadoCivil']))

        # Changing field 'Unidade.cidade'
        db.alter_column('Unidade', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Cidade']))

        # Changing field 'TituloEleitor.zona'
        db.alter_column('TituloEleitor', 'zona', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'TituloEleitor.secao'
        db.alter_column('TituloEleitor', 'secao', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'TituloEleitor.cidade'
        db.alter_column('TituloEleitor', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Cidade']))

        # Changing field 'TituloEleitor.titulo'
        db.alter_column('TituloEleitor', 'titulo', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'TituloEleitor.pessoa'
        db.alter_column('TituloEleitor', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'NecessidadeEspecial.descricao'
        db.alter_column('NecessidadeEspecial', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Cidade.uf'
        db.alter_column('Cidade', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.UF']))

        # Changing field 'Cidade.nome'
        db.alter_column('Cidade', 'nome', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'AreaAtuacao.descricao'
        db.alter_column('AreaAtuacao', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Categoria.descricao'
        db.alter_column('Categoria', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'UF.pais'
        db.alter_column('UF', 'pais_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pais']))

        # Changing field 'UF.abreviacao'
        db.alter_column('UF', 'abreviacao', self.gf('django.db.models.fields.CharField')(default=None, max_length=2))

        # Changing field 'UF.nome'
        db.alter_column('UF', 'nome', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Ponto.hora'
        db.alter_column('Ponto', 'hora', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=None))

        # Changing field 'Ponto.capacitando'
        db.alter_column('Ponto', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Capacitando']))

        # Changing field 'Ponto.user'
        db.alter_column('Ponto', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'Ponto.data'
        db.alter_column('Ponto', 'data', self.gf('django.db.models.fields.DateField')(auto_now=True, default=None))

        # Changing field 'Ponto.tipo_ponto'
        db.alter_column('Ponto', 'tipo_ponto_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.TipoPonto']))

        # Changing field 'Etnia.descricao'
        db.alter_column('Etnia', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Filiacao.pessoa'
        db.alter_column('Filiacao', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'Filiacao.cpf'
        db.alter_column('Filiacao', 'cpf', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Filiacao.nome'
        db.alter_column('Filiacao', 'nome', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Desligamento.capacitando'
        db.alter_column('Desligamento', 'capacitando_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Capacitando']))

        # Changing field 'RegistroGeral.pessoa'
        db.alter_column('RegistroGeral', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'ServicoMilitar.pessoa'
        db.alter_column('ServicoMilitar', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'ServicoMilitar.ano'
        db.alter_column('ServicoMilitar', 'ano', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'ServicoMilitar.uf'
        db.alter_column('ServicoMilitar', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.UF']))

        # Changing field 'Endereco.endereco'
        db.alter_column('Endereco', 'endereco', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Endereco.cidade'
        db.alter_column('Endereco', 'cidade_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Cidade']))

        # Changing field 'Endereco.cep'
        db.alter_column('Endereco', 'cep', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Endereco.bairro'
        db.alter_column('Endereco', 'bairro', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'TipoIdentidade.descricao'
        db.alter_column('TipoIdentidade', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Email.endereco'
        db.alter_column('Email', 'endereco', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Email.pessoa'
        db.alter_column('Email', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'CategoriaCNH.categoria'
        db.alter_column('CategoriaCNH', 'categoria', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Pais.nome'
        db.alter_column('Pais', 'nome', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Reservista.serie'
        db.alter_column('Reservista', 'serie', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Reservista.orgao'
        db.alter_column('Reservista', 'orgao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Reservista.dispensa_incorporacao'
        db.alter_column('Reservista', 'dispensa_incorporacao', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'Reservista.unidade_alistamento'
        db.alter_column('Reservista', 'unidade_alistamento', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Reservista.pessoa'
        db.alter_column('Reservista', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'Reservista.certificado'
        db.alter_column('Reservista', 'certificado', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'CNH.validade'
        db.alter_column('CNH', 'validade', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'CNH.categoria_cnh'
        db.alter_column('CNH', 'categoria_cnh_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.CategoriaCNH']))

        # Changing field 'CNH.numero'
        db.alter_column('CNH', 'numero', self.gf('django.db.models.fields.BigIntegerField')(default=None))

        # Changing field 'CNH.data_emissao'
        db.alter_column('CNH', 'data_emissao', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'CNH.pessoa'
        db.alter_column('CNH', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'CNH.uf'
        db.alter_column('CNH', 'uf_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.UF']))

        # Changing field 'TipoPonto.descricao'
        db.alter_column('TipoPonto', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Especialidade.descricao'
        db.alter_column('Especialidade', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Turno.saida_lanche'
        db.alter_column('Turno', 'saida_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=None))

        # Changing field 'Turno.saida'
        db.alter_column('Turno', 'saida', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=None))

        # Changing field 'Turno.descricao'
        db.alter_column('Turno', 'descricao', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Turno.entrada_lanche'
        db.alter_column('Turno', 'entrada_lanche', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=None))

        # Changing field 'Turno.entrada'
        db.alter_column('Turno', 'entrada', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=None))

        # Changing field 'Telefone.pessoa'
        db.alter_column('Telefone', 'pessoa_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.Pessoa']))

        # Changing field 'Telefone.tipo_telefone'
        db.alter_column('Telefone', 'tipo_telefone_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['modelos.TipoTelefone']))

        # Changing field 'Telefone.numero'
        db.alter_column('Telefone', 'numero', self.gf('django.db.models.fields.BigIntegerField')(default=None))

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
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.capacitando': {
            'Meta': {'object_name': 'Capacitando', 'db_table': "'Capacitando'"},
            'area_atuacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.AreaAtuacao']", 'null': 'True'}),
            'atualizacao_cadastral': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Categoria']", 'null': 'True'}),
            'data_registro': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'especialidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Especialidade']", 'null': 'True'}),
            'familia': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'hora_registro': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacao_social': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'inicio_atividades': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'matricula': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'necessidade_especial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.NecessidadeEspecial']", 'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'renda_per_capita': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'responsavel_familia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'turno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Turno']", 'null': 'True'}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Unidade']", 'null': 'True'})
        },
        u'modelos.carteiratrabalho': {
            'Meta': {'object_name': 'CarteiraTrabalho', 'db_table': "'CarteiraTrabalho'"},
            'ctps': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'serie': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'modelos.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "'Categoria'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.categoriacnh': {
            'Meta': {'object_name': 'CategoriaCNH', 'db_table': "'CategoriaCNH'"},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.cidade': {
            'Meta': {'object_name': 'Cidade', 'db_table': "'Cidade'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'})
        },
        u'modelos.cnh': {
            'Meta': {'object_name': 'CNH', 'db_table': "'CNH'"},
            'categoria_cnh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.CategoriaCNH']", 'null': 'True'}),
            'data_emissao': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'}),
            'validade': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'modelos.desligamento': {
            'Meta': {'object_name': 'Desligamento', 'db_table': "'Desligamento'"},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']", 'null': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.email': {
            'Meta': {'object_name': 'Email', 'db_table': "'Email'"},
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'})
        },
        u'modelos.endereco': {
            'Meta': {'object_name': 'Endereco', 'db_table': "'Endereco'"},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'cep': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'null': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.especialidade': {
            'Meta': {'object_name': 'Especialidade', 'db_table': "'Especialidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.estadocivil': {
            'Meta': {'object_name': 'EstadoCivil', 'db_table': "'EstadoCivil'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.etnia': {
            'Meta': {'object_name': 'Etnia', 'db_table': "'Etnia'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.filiacao': {
            'Meta': {'object_name': 'Filiacao', 'db_table': "'Filiacao'"},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'})
        },
        u'modelos.nacionalidade': {
            'Meta': {'object_name': 'Nacionalidade', 'db_table': "'Nacionalidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.naturalidade': {
            'Meta': {'object_name': 'Naturalidade', 'db_table': "'Naturalidade'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']", 'null': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'})
        },
        u'modelos.necessidadeespecial': {
            'Meta': {'object_name': 'NecessidadeEspecial', 'db_table': "'NecessidadeEspecial'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.pais': {
            'Meta': {'object_name': 'Pais', 'db_table': "'Pais'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'modelos.pessoa': {
            'Meta': {'object_name': 'Pessoa', 'db_table': "'Pessoa'"},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Endereco']", 'null': 'True'}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.EstadoCivil']", 'null': 'True'}),
            'etnia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Etnia']", 'null': 'True'}),
            'filhos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Nacionalidade']", 'null': 'True'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Naturalidade']", 'null': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'sexo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_identidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoIdentidade']", 'null': 'True'})
        },
        u'modelos.ponto': {
            'Meta': {'object_name': 'Ponto', 'db_table': "'Ponto'"},
            'capacitando': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Capacitando']", 'null': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_ponto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoPonto']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'modelos.registrogeral': {
            'Meta': {'object_name': 'RegistroGeral', 'db_table': "'RegistroGeral'"},
            'data_expedicao': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgao_expedidor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'rg': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'})
        },
        u'modelos.reservista': {
            'Meta': {'object_name': 'Reservista', 'db_table': "'Reservista'"},
            'certificado': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'dispensa_incorporacao': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'serie': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'unidade_alistamento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'modelos.servicomilitar': {
            'Meta': {'object_name': 'ServicoMilitar', 'db_table': "'ServicoMilitar'"},
            'ano': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.UF']", 'null': 'True'})
        },
        u'modelos.telefone': {
            'Meta': {'object_name': 'Telefone', 'db_table': "'Telefone'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'tipo_telefone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.TipoTelefone']", 'null': 'True'})
        },
        u'modelos.tipoidentidade': {
            'Meta': {'object_name': 'TipoIdentidade', 'db_table': "'TipoIdentidade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tipoponto': {
            'Meta': {'object_name': 'TipoPonto', 'db_table': "'TipoPonto'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tipotelefone': {
            'Meta': {'object_name': 'TipoTelefone', 'db_table': "'TipoTelefone'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modelos.tituloeleitor': {
            'Meta': {'object_name': 'TituloEleitor', 'db_table': "'TituloEleitor'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pessoa']", 'null': 'True'}),
            'secao': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'titulo': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'zona': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'modelos.turno': {
            'Meta': {'object_name': 'Turno', 'db_table': "'Turno'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entrada': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'entrada_lanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saida': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'saida_lanche': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'modelos.uf': {
            'Meta': {'object_name': 'UF', 'db_table': "'UF'"},
            'abreviacao': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Pais']", 'null': 'True'})
        },
        u'modelos.unidade': {
            'Meta': {'object_name': 'Unidade', 'db_table': "'Unidade'"},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modelos.Cidade']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['modelos']