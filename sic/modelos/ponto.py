# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from modelos.capacitando import Capacitando


class TipoPonto(models.Model):

    class Meta:
        db_table = 'TipoPonto'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255)


class Ponto(models.Model):

    class Meta:
        db_table = 'Ponto'

    def __unicode__(self):
        return '%s - %s: %s' % (self.data, self.hora, self.capacitando)

    data = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    tipo_ponto = models.ForeignKey(TipoPonto)
    capacitando = models.ForeignKey(Capacitando)
    user = models.ForeignKey(User)
