# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from modelos.capacitando import Capacitando
from ponto import registrar_ponto


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
        capacitando = Capacitando.objects.get(
            matricula=matricula_ponto, status=1)

        registrar_ponto(capacitando, user)

    except ObjectDoesNotExist:
        return render_to_response(
            'ponto.html', {
                'capacitando_inativo': True
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        'home.html',
        context_instance=RequestContext(request),
    )
