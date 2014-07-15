# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required
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


def obter_lista_departamentos_json(request):
    departamentos_json = serializers.serialize(
        'json', Departamento.objects.all())
    departamentos_list = json.loads(departamentos_json)
    return render_to_response(
        json.dumps({'departamentos': departamentos_list}),
        content_type="application/json")


def obter_lista_funcionarios_json(request):
    funcionarios_json = serializers.serialize(
        'json', Funcionario.objects.all())
    funcionarios_list = json.loads(funcionarios_json)
    return render_to_response(
        json.dumps({'funcionarios': funcionarios_list}),
        content_type="application/json")
