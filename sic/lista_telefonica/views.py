# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from modelos.funcionario import Departamento, Funcionario
import json


@login_required(login_url='/login')
def listar_telefones(request):
    # lista_departamentos = obter_lista_departamentos()
    return render_to_response('lista_telefonica.html',
                              context_instance=RequestContext(request))


def obter_lista_departamentos_json(request):
    return render_to_response(json.dumps(Departamento.objects.all()),
                              content_type="application/json")


def obter_lista_funcionarios_por_departamento(request):
    lista_departamentos = {}
    lista_funcionarios = {}

    lista_funcionarios_por_departamento = {}

    for departamento in Departamento.objects.all():
        lista_funcionarios = {}
        for funcionario in \
                Funcionario.objects.filter(departamento_id=departamento.id):
            lista_funcionarios[funcionario.id] = funcionario
        lista_departamentos[departamento.id] = lista_funcionarios

    return render_to_response(lista_funcionarios_por_departamento)


def obter_funcionarios_json(request):
    return render_to_response(json.dumps(Funcionario.objects.all()),
                              content_type="application/json")
