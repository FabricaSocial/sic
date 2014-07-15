# -*- encoding: utf-8 -*-

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
    return json.dumps(Departamento.objects.all())


def obter_lista_departamento_por_nome(nome):
    return Departamento.objects.filter(descricao=nome)


def obter_lista_funcionarios_por_departamento():
    lista_departamentos = {}
    lista_funcionarios = {}

    lista_funcionarios_por_departamento = {}

    for departamento in Departamento.objects.all():
        lista_funcionarios = {}
        for funcionario in \
                Funcionario.objects.filter(departamento_id=departamento.id):
            lista_funcionarios[funcionario.id] = funcionario
        lista_departamentos[departamento.id] = lista_funcionarios

    return lista_funcionarios_por_departamento


def obter_funcionarios_json():
    return json.dumps(Funcionario.objects.all())


def obter_pessoa_por_cpf(cpf):
    return Pessoa.objects.get(cpf=cpf)
