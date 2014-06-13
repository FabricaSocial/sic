# -*- coding: utf-8 -*-

from django.db import models

from modelos.dados_pessoa import Cidade, Pessoa
from modelos.ponto import Turno


class Categoria(models.Model):

    class Meta:
        db_tabe = 'Categoria'

    def __unicode__(self):
        self.descricao

    descricao = models.CharField(max_length=255)


class NecessidadeEspecial(models.Model):

    class Meta:
        db_table = 'NecessidadeEpecial'

    def __unicode__(self):
        pass

    descricao = models.CharField(max_length=255)


class Especialidade(models.Model):

    class Meta:
        db_table = 'Especialidades'

    def __unicode__(self):
        pass

    descricao = models.CharField(max_length=255)


class AreaAtuacao(models.Model):

    class Meta:
        db_table = 'AreaAtuacao'

    def __unicode__(self):
        pass

    descricao = models.CharField(max_length=255)


class Unidade(models.Model):

    class Meta:
        db_table = 'Unidade'

    def __unicode__(self):
        self.cidade

    cidade = models.ForeignKey(Cidade)


class Capacitando(models.Model):

    class Meta:
        db_table = 'Capacitando'

    def __unicode__(self):
        pass

    matricula = models.BigIntegerField()
    identificacao_social = models.BigIntegerField()
    responsavel_familia = models.BooleanField()
    familia = models.BigIntegerField()
    renda_per_capita = models.FloatField()
    atualizacao_cadastral = models.DateField()
    inicio_atividades = models.DateField()
    status = models.BooleanField()
    data_registro = models.DateField()
    hora_registro = models.TimeField()
    area_atuacao = models.ForeignKey(AreaAtuacao)
    especialidade = models.ForeignKey(Especialidade)
    pessoa = models.ForeignKey(Pessoa)
    necessidade_especial = models.ForeignKey(NecessidadeEspecial)
    categoria = models.ForeignKey(Categoria)
    unidade = models.ForeignKey(Unidade)
    turno = models.ForeignKey(Turno)


class Desligamento(models.Model):

    class Meta:
        db_table = 'Desligamento'

    def __unicode__(self):
        self.capacitando

    data = models.DateField()
    capacitando = models.ForeignKey(Capacitando)
