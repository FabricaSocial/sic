# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from modelos.capacitando import Turno


@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.groups.filter(name='gerencia').count():
        gerencia = True
    else:
        gerencia = False

    return render_to_response(
        'home.html',
        {'gerencia': gerencia},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def painel_controle(request):
    turnos = Turno.objects.all()

    return render_to_response(
        'painel_controle.html',
        {'turnos': turnos},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def alterar_ponto(request):
    salvar_alteracoes(request)

    turnos = Turno.objects.all()

    return render_to_response(
        'painel_controle.html',
        {'turnos': turnos},
        context_instance=RequestContext(request))


def salvar_alteracoes(request):
    turno_id = request.POST['id']
    turno = Turno.objects.get(pk=turno_id)

    print turno.entrada
    print turno.saida_lanche
    print turno.entrada_lanche
    print turno.saida

    turno.entrada = request.POST['entrada']
    turno.entrada_tolerancia = request.POST['entrada_tolerancia']
    turno.saida_lanche = request.POST['saida_lanche']
    turno.saida_lanche_tolerancia = request.POST['saida_lanche_tolerancia']
    turno.entrada_lanche = request.POST['entrada_lanche']
    turno.entrada_lanche_tolerancia = request.POST['entrada_lanche_tolerancia']
    turno.saida = request.POST['saida']
    turno.saida_tolerancia = request.POST['saida_tolerancia']

    print turno.entrada
    print turno.saida_lanche
    print turno.entrada_lanche
    print turno.saida

    turno.save()
