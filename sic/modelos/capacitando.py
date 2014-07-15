# -*- coding: utf-8 -*-

from django.db import models

from modelos.pessoa import Pessoa


class Categoria(models.Model):

    class Meta:
        db_table = 'Categoria'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class NecessidadeEspecial(models.Model):

    class Meta:
        db_table = 'NecessidadeEspecial'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Especialidade(models.Model):

    class Meta:
        db_table = 'Especialidade'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class AreaAtuacao(models.Model):

    class Meta:
        db_table = 'AreaAtuacao'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Turno(models.Model):

    class Meta:
        db_table = 'Turno'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)
    entrada = models.TimeField(null=True)
    entrada_tolerancia = models.TimeField(null=True)
    saida_lanche = models.TimeField(null=True)
    saida_lanche_tolerancia = models.TimeField(null=True)
    entrada_lanche = models.TimeField(null=True)
    entrada_lanche_tolerancia = models.TimeField(null=True)
    saida = models.TimeField(null=True)
    saida_tolerancia = models.TimeField(null=True)


class Capacitando(models.Model):

    class Meta:
        db_table = 'Capacitando'

    def __unicode__(self):
        return self.pessoa.nome

    matricula = models.BigIntegerField(null=True)
    identificacao_social = models.BigIntegerField(null=True)
    responsavel_familia = models.BooleanField(default=False)
    familia = models.BigIntegerField(null=True)
    renda_per_capita = models.FloatField(null=True)
    atualizacao_cadastral = models.DateField(null=True)
    inicio_atividades = models.DateField(null=True)
    status = models.BooleanField(default=True)
    data_registro = models.DateField(null=True)
    hora_registro = models.TimeField(null=True)
    area_atuacao = models.ForeignKey(AreaAtuacao, null=True)
    especialidade = models.ForeignKey(Especialidade, null=True)
    pessoa = models.ForeignKey(Pessoa, null=True)
    necessidade_especial = models.ForeignKey(NecessidadeEspecial, null=True)
    categoria = models.ForeignKey(Categoria, null=True)
    turno = models.ForeignKey(Turno, null=True)


class Desligamento(models.Model):

    class Meta:
        db_table = 'Desligamento'

    def __unicode__(self):
        return self.capacitando

    data = models.DateField()
    capacitando = models.ForeignKey(Capacitando, null=True)
