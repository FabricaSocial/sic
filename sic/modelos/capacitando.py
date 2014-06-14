# -*- coding: utf-8 -*-

from django.db import models

from modelos.pessoa import Cidade, Pessoa


class Categoria(models.Model):

    class Meta:
        db_table = 'Categoria'

    def __unicode__(self):
        self.descricao

    descricao = models.CharField(max_length=255)


class NecessidadeEspecial(models.Model):

    class Meta:
        db_table = 'NecessidadeEspecial'

    def __unicode__(self):
        pass

    descricao = models.CharField(max_length=255)


class Especialidade(models.Model):

    class Meta:
        db_table = 'Especialidade'

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


class Turno(models.Model):

    class Meta:
        db_table = 'Turno'

    def __unicode__(self):
        self.descricao

    descricao = models.CharField(max_length=255)
    entrada = models.TimeField(auto_now=True)
    saida_lanche = models.TimeField(auto_now=True)
    entrada_lanche = models.TimeField(auto_now=True)
    saida = models.TimeField(auto_now=True)


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
