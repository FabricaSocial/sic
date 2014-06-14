# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from access_db.models import Tabfuncionarios

from ponto import obter_turno


@login_required(login_url='/login/')
def ponto(request):
    return render_to_response(
        'ponto.html',
        context_instance=RequestContext(request),
    )


@login_required(login_url='/login/')
def registro(request):
    matricula_ponto = request.POST['matricula']
    user = request.user

    try:
        capacitando = Tabfuncionarios.objects.get(
            matricula=matricula_ponto, status="ATIVO(A)"
        )
        capacitando.user = user
        obter_turno(capacitando)

    except Exception, e:
        return render_to_response(
            'ponto.html', {
                'capacitando_inativo': True
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        'home.html',
        context_instance=RequestContext(request),
    )
