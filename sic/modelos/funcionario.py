# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from modelos.pessoa import Pessoa
from modelos.administrativo import Ramal, Departamento


class TipoAudit(models.Model):

    class Meta:
        db_table = 'TipoAudit'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Lotacao(models.Model):

    class Meta:
        db_table = 'Lotacao'

    def __unicode__(self):
        return self.descricao

    descricao = models.CharField(max_length=255, null=True)


class Cargo(models.Model):

    class Meta:
        db_table = 'Cargo'

    def __unicode__(self):
        return self.cargo_efetivo

    cargo_efetivo = models.CharField(max_length=255, null=True)
    lotacao = models.ForeignKey(Lotacao, null=True)


class LotacaoRamal(models.Model):

    class Meta:
        db_table = 'LotacaoRamal'

    def __unicode(self):
        return self.ramal.ramal + ' - ' \
            + self.lotacao.descricao

    ramal = models.ForeignKey(Ramal, null=True)
    lotacao = models.ForeignKey(Lotacao, null=True)


class Funcionario(models.Model):

    class Meta:
        db_table = 'Funcionario'

    def __unicode__(self):
        return self.pessoa.nome

    matricula = models.IntegerField(null=True)
    status = models.BooleanField(default=True)
    pessoa = models.ForeignKey(Pessoa, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
    departamento = models.ForeignKey(Departamento, null=True)
    usuario = models.ForeignKey(User, null=True)


class FuncionarioAudit(models.Model):

    class Meta:
        db_table = 'FuncionarioAudit'

    def __unicode__(self):
        return self.timestamp + ' - ' + self.funcionario.nome \
            + ' - ' + self.tipo_audit.descricao

    timestamp = models.DateTimeField(null=True)
    funcionario = models.ForeignKey(Funcionario, null=True)
    usuario = models.ForeignKey(User, null=True)
    tipo_audit = models.ForeignKey(TipoAudit, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
    usuario = models.ForeignKey(User, null=True)
    tipo_audit = models.ForeignKey(TipoAudit, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
