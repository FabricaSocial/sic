# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required


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


def pagina_nao_encontrada(request):
    mensagem_erro = 'A página solicitada não foi encontrada :('

    return render(request, 'home.html', {
        'modal_erro': True,
        'mensagem_erro': mensagem_erro})


def acesso_negado(request):
    mensagem_erro = 'Você não tem permissão para acessar essa página :('

    return render(request, 'home.html', {
        'modal_erro': True,
        'mensagem_erro': mensagem_erro})


def erro_no_sistema(request):
    mensagem_erro = 'Ocorreu um erro no sistema :('

    return render(request, 'home.html', {
        'modal_erro': True,
        'mensagem_erro': mensagem_erro})
