# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from modelos.administrativo import CoordenadoriaAdjunta


@login_required(login_url='/login')
def listar_telefones(request):
    coordenadorias_adjuntas = CoordenadoriaAdjunta.obter_lista()
    return render_to_response('lista_telefonica.html',
                              {'coordenadorias_adjuntas':
                               coordenadorias_adjuntas},
                              context_instance=RequestContext(request))
