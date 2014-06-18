# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from modelos.capacitando import Capacitando
from ponto import registrar_ponto, verifica_tolerancia


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


def registrar_ponto_ajax(request, matricula):
    mensagem = ""

    try:
        capacitando = Capacitando.objects.get(
            matricula=matricula)

        ponto = registrar_ponto(capacitando, request.user)

        tolerancia = verifica_tolerancia(capacitando, ponto)
        
        if capacitando.status:
            if tolerancia:
                mensagem = "Ponto registrado com sucesso!"
            else:
                mensagem = "Fora do horário de ponto permitido!"
        else:
            mensagem = "Capacitando Inativo."

    except ObjectDoesNotExist:
        mensagem = "Capacitando não cadastrado."

    

    return HttpResponse(mensagem)
