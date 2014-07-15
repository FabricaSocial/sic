# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from modelos.funcionario import Departamento, Funcionario
import json


@login_required(login_url='/login')
def listar_telefones(request):
    # lista_departamentos = obter_lista_departamentos()
    pass


def obter_lista_departamentos_json():
    return HttpResponse(json.dumps(Departamento.objects.all()),
                        content_type="application/json")


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


def obter_funcionarios_json(request):
    return HttpResponse(json.dumps(Funcionario.objects.all()),
                        content_type="application/json")
