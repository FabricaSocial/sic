# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from modelos.funcionario import Departamento, Funcionario
from modelos.pessoa import Pessoa
import json


@login_required(login_url='/login')
def listar_telefones(request):
    # lista_departamentos = obter_lista_departamentos()
    pass


def obter_lista_departamentos():
    return Departamento.objects.all()


def obter_lista_departamentos_json():
    lista_departamentos = Departamento.objects.all()
    lista_departamentos_json = json.dumps(lista_departamentos)
    return lista_departamentos_json


def obter_lista_funcionarios_por_departamento():
    lista_departamentos = {}
    lista_funcionarios = {}

    lista_funcionarios_por_departamento = {}

    for departamento in Departamento.objects.all():
        lista_funcionarios = {}
        for funcionario in \
                Funcionario.objects.filter(departamento_id=departamento.id):
            lista_funcionarios[funcionario.id] = funcionario.pessoa.nome
        lista_departamentos[departamento.id] = lista_funcionarios

    return lista_funcionarios_por_departamento


def obter_funcionarios_json():
    lista_funcionarios = Funcionario.objects.all()
    lista_funcionarios_json = json.dumps(lista_funcionarios)
    return lista_funcionarios_json


def obter_pessoa_por_cpf(cpf):
    return Pessoa.objects.get(cpf=cpf)
