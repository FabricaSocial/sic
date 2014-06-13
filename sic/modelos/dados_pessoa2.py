# -*- coding: utf-8 -*-

from django.db import models


class Pessoa(models.Model):

    class Meta:
        db_table = 'Pessoa'

    def __unicode__(self):
        self.nome

    cpf = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    sexo = models.BooleanField()
    filhos = models.BooleanField()
    foto = models.CharField(max_length=255)
    etnia = models.ForeignKey(Etnia)
    tipo_identidade = models.ForeignKey(TipoIdentidade)
    estado_civil = models.ForeignKey(EstadoCivil)
    endereco = models.ForeignKey(Endereco)
    nacionalidade = models.ForeignKey(Nacionalidade)
    naturalidade = models.ForeignKey(Naturalidade)
