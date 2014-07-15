# -*- coding: utf-8 -*-

from django.db import models

from modelos.pessoa import Cidade


class Ramal(models.Model):

    class Meta:
        db_table = 'Ramal'

    def __unicode__(self):
        return self.ramal

    ramal = models.IntegerField(null=True)


class Coordenadoria(models.Model):

    class Meta:
        db_table = 'Coordenadoria'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)
    abreviacao = models.CharField(max_length=255, null=True)


class CoordenadoriaAdjunta(models.Model):

    class Meta:
        db_table = 'CoordenadoriaAdjunta'

    def __unicode__(self):
        return self.descricao

    @classmethod
    def obter_lista(cls):
        return CoordenadoriaAdjunta.objects.all()

    descricao = models.CharField(max_length=255, null=True)
    abreviacao = models.CharField(max_length=255, null=True)
    coordenadoria = models.ForeignKey(Coordenadoria, null=True)


class Unidade(models.Model):

    class Meta:
        db_table = 'Unidade'

    def __unicode__(self):
        return self.cidade

    cidade = models.ForeignKey(Cidade, null=True)
    ramal = models.ForeignKey(Ramal, null=True)


class Departamento(models.Model):

    class Meta:
        db_table = 'Departamento'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)
    abreviacao = models.CharField(max_length=255, null=True)
    coordenadoria_adjunta = models.ForeignKey(CoordenadoriaAdjunta, null=True)
    ramal = models.ForeignKey(Ramal, null=True)
    unidade = models.ForeignKey(Unidade, null=True)
