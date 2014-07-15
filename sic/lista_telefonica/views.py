# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from modelos.funcionario import Departamento
import json


@login_required(login_url='/login')
def listar_telefones(request):
    return render_to_response('lista_telefonica.html',
                              context_instance=RequestContext(request))


def obter_lista_departamentos_json(request):
    return render_to_response(json.dumps(Departamento.objects.all()),
                              content_type="application/json")
