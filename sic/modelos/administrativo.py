# -*- coding: utf-8 -*-

from django.db import models


class Ramal(models.Model):

    class Meta:
        db_table = 'Ramal'

    def __unicode__(self):
        return "%s" % (self.ramal)

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

    def obter_departamentos(self):
        return Departamento.objects.filter(
            coordenadoria_adjunta_id=self.id).order_by('descricao')

    descricao = models.CharField(max_length=255, null=True)
    abreviacao = models.CharField(max_length=255, null=True)
    coordenadoria = models.ForeignKey(Coordenadoria, null=True)
    departamentos = property(obter_departamentos)


class Departamento(models.Model):

    class Meta:
        db_table = 'Departamento'

    def __unicode__(self):
        return self.descricao

    def obter_funcionarios(self):
        from modelos.funcionario import Funcionario

        return Funcionario.objects.filter(departamento_id=self.id)

    descricao = models.CharField(max_length=255, null=True)
    abreviacao = models.CharField(max_length=255, null=True)
    coordenadoria_adjunta = models.ForeignKey(CoordenadoriaAdjunta, null=True)
    ramal = models.ForeignKey(Ramal, null=True)
    funcionarios = property(obter_funcionarios)
