# -*- coding: utf-8 -*-

from django.db import models
from modelos.capacitando import Capacitando


class TipoPonto(models.Model):

    class Meta:
        db_table = 'TipoPonto'

    def __unicode__(self):
        self.descricao

    descricao = models.CharField(max_length=255)


class Ponto(models.Model):

    class Meta:
        db_table = 'Ponto'

    def __unicode__(self):
        self.capacitando.nome

    data = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    tipo_ponto = models.ForeignKey(TipoPonto)
    capacitando = models.ForeignKey(Capacitando)


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
