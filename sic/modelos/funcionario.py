# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from modelos.pessoa import Pessoa
from modelos.administrativo import Departamento, Ramal


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


class Funcionario(models.Model):

    class Meta:
        db_table = 'Funcionario'

    def __unicode__(self):
        return self.pessoa.nome

    def natural_key(self):
        return dict(id=self.id, departamento=self.departamento,
                    ramal=self.ramal)

    @classmethod
    def busca_dinamica_por_nome(cls, nome):
        return Funcionario.objects.filter(
            pessoa__nome__icontains=nome, status=True)

    matricula = models.IntegerField(null=True)
    status = models.BooleanField(default=True)
    pessoa = models.OneToOneField(Pessoa, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
    departamento = models.ForeignKey(Departamento, null=True)
    usuario = models.OneToOneField(User, null=True)
    ramal = models.ForeignKey(Ramal, null=True)


class FuncionarioAudit(models.Model):

    class Meta:
        db_table = 'FuncionarioAudit'

    def __unicode__(self):
        return self.timestamp + ' - ' + self.funcionario.nome \
            + ' - ' + self.tipo_audit.descricao

    timestamp = models.DateTimeField(null=True, auto_now=True)
    funcionario = models.ForeignKey(Funcionario, null=True)
    usuario = models.ForeignKey(User, null=True)
    tipo_audit = models.ForeignKey(TipoAudit, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
    usuario = models.ForeignKey(User, null=True)
    tipo_audit = models.ForeignKey(TipoAudit, null=True)
    cargo = models.ForeignKey(Cargo, null=True)
