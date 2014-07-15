# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from modelos.administrativo import CoordenadoriaAdjunta, Departamento
from modelos.funcionario import Funcionario
import json


@login_required(login_url='/login')
def listar_telefones(request):
    coordenadorias_adjuntas = CoordenadoriaAdjunta.obter_lista()
    return render_to_response('lista_telefonica.html',
                              {'coordenadorias_adjuntas':
                               coordenadorias_adjuntas},
                              context_instance=RequestContext(request))


@login_required(login_url='/login')
def obter_lista_departamentos_json(request):
    departamentos_json = serializers.serialize(
        'json', Departamento.objects.all(), use_natural_keys=True)
    departamentos_list = json.loads(departamentos_json)
    return HttpResponse(
        json.dumps({'departamentos': departamentos_list}),
        content_type="application/json")


@login_required(login_url='/login')
def obter_lista_funcionarios_json(request, nome):
    funcionarios = Funcionario.busca_dinamica_por_nome(nome)

    if funcionarios.count() > 0 and len(nome):
        funcionarios_json = serializers.serialize(
            'json', funcionarios, use_natural_keys=True)

        funcionarios_list = json.loads(funcionarios_json)
        json_funcionarios = json.dumps({'funcionarios': funcionarios_list}),

        return HttpResponse(json_funcionarios, content_type="application/json")

    else:
        return HttpResponseBadRequest()
